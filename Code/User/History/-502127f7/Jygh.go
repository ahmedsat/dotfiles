package types

import (
	"encoding/json"
	"encoding/xml"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"reflect"
	"strings"

	"github.com/ahmedsat/erp-reports/utils"
	"github.com/kokardy/saxlike"
)

type farm struct {
	name    string
	sectors []sector
}

type sector struct {
	name  string
	plots []plot
}

type plot struct {
	name string
}

type handler struct {
	saxlike.VoidHandler
	depths       int
	read         bool
	farm         *farm
	activeSector *sector
	activePlot   *plot
}

// called when XML tag start
func (h *handler) StartElement(element xml.StartElement) {
	// fmt.Println(element.Name.Local)
	switch element.Name.Local {
	case "ul":
		if h.depths < 1 {
			h.farm = &farm{}
			h.depths = 1
			break
		}
		if h.depths == 1 {
			h.activeSector = &sector{}
			h.depths = 2
			break
		}
		if h.depths == 2 {
			h.activePlot = &plot{}
			h.depths = 3
			break
		}
	case "span":
		h.read = true
	}
}

// called when XML tag end
func (h *handler) EndElement(element xml.EndElement) {
	switch element.Name.Local {
	case "ul":

		if h.depths == 2 {
			h.farm.sectors = append(h.farm.sectors, *h.activeSector)
		}
		if h.depths == 3 {
			h.activeSector.plots = append(h.activeSector.plots, *h.activePlot)
		}
		h.depths--
	case "span":
		h.read = false
	}
}

// called when the parser encount chardata
func (h *handler) CharData(data xml.CharData) {

	if !h.read {
		return
	}

	if h.depths == 3 {
		h.activePlot.name = string(data)
		return
	}

	if h.depths == 2 {
		h.activeSector.name = string(data)
		return
	}

	if h.depths == 1 {
		h.farm.name = string(data)
		return
	}

}

func (f *Farm) UpdateFarmStructure() (err error) {
	URL := "https://erp.sekem.com:86/api/method/get_structure/"
	form := url.Values{}
	form.Add("farm", f.Name)
	form.Add("arabic", f.ArabicName)

	c := http.Client{}
	req, err := http.NewRequest("GET", URL+fmt.Sprint("?"+form.Encode()), nil)
	if err != nil {
		return
	}

	cookies, err := utils.GetCookies()
	if err != nil {
		return
	}
	req.Header.Add("Cookie", cookies)
	req.Header.Add("Content-Type", "application/json")
	req.Header.Add("Accept", "application/json")

	resp, err := c.Do(req)
	if err != nil {
		return
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		err = fmt.Errorf("ERROR: request to %s return status code of %d", URL, resp.StatusCode)
		return
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return
	}

	m := &Message{}
	err = json.Unmarshal(body, m)
	if err != nil {
		return
	}

	h := handler{}
	p := saxlike.NewParser(strings.NewReader(m.Message), &h)
	p.SetHTMLMode()
	err = p.Parse()
	if err != nil {
		return
	}

	if len(h.farm.sectors[0].plots) > 0 {
		f.FarmStructure = true
	}

	return
}

func (f *Farm) UpdateFarmMap() (err error) {

	URL := "https://erp.sekem.com:86/api/method/return_polygons?all=ON&farm=" + f.Name

	res, err := utils.RestGet(URL, utils.NewFilters(""), 0, 0, true)
	if err != nil {
		return
	}

	bytes, err := io.ReadAll(res.Body)
	if err != nil {
		return
	}

	f.FarmMap = !reflect.DeepEqual(bytes, []byte{0x7b, 0x22, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x22, 0x3a, 0x7b, 0x7d, 0x7d})

	return
}
