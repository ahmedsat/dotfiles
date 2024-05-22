package utils

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strings"
)

type Farm struct {
	Name                string  `json:"name"`
	Owner               string  `json:"owner"`
	Creation            string  `json:"creation"`
	Modified            string  `json:"modified"`
	ModifiedBy          string  `json:"modified_by"`
	Idx                 int     `json:"idx"`
	DocStatus           int     `json:"docstatus"`
	DocName             string  `json:"docname"`
	Type                string  `json:"type"`
	IsPlotOfSector      string  `json:"is_plot_of_sector"`
	ArabicName          string  `json:"arabic_name"`
	UpscalingProject    string  `json:"upscaling_project"`
	Region              string  `json:"region"`
	ParentFarm          string  `json:"parent_farm"`
	Category            string  `json:"gategory"`
	FarmName            string  `json:"farm_name"`
	FarmAreaFeddan      float64 `json:"farm_area__feddan"`
	IsInternal          int     `json:"is_internal_farm"`
	Company             string  `json:"company"`
	FarmId              string  `json:"farm_id"`
	FarmOwner           string  `json:"farm_owner"`
	FarmOwnership       string  `json:"farm_ownership"`
	Phone               string  `json:"phone"`
	TotalFarmer         int     `json:"total_farmers"`
	Latitude            string  `json:"latitude"`
	Longitude           string  `json:"longitude"`
	YearOfReclamation   int     `json:"year_of_reclamation"`
	SoilStatus          string  `json:"soil_status"`
	TotalTrees          int     `json:"total_trees"`
	Lft                 int     `json:"lft"`
	Rgt                 int     `json:"rgt"`
	OldParent           string  `json:"old_parent"`
	SectorAreaInFeddan  float64 `json:"sector_area_in_feddan"`
	PlotAreaInFeddan    float64 `json:"plot_area_in_feddan"`
	SubPlotAreaInFeddan float64 `json:"sub_plot_area_in_feddan"`
	FarmApplication     string  `json:"farm_application"`
	IsGroup             int     `json:"is_group"`
	EN_name             string  `json:"en_name"`
	Doctype             string  `json:"doctype"`
}

func RestGet(URL string, filters filters, start, limit uint, all bool) (resp *http.Response, err error) {

	URL = strings.ReplaceAll(URL, " ", "%20")

	form := url.Values{}

	if all {
		form.Add("fields", "[\"*\"]")
	}

	form.Add("filters", filters.String())
	form.Add("limit_start", fmt.Sprint(start))
	form.Add("limit_page_length", fmt.Sprint(limit))

	if filters.doctype != "" {
		URL += fmt.Sprint("?" + form.Encode())
	}

	c := http.Client{}
	req, err := http.NewRequest("GET", URL, nil)
	if err != nil {
		return
	}

	cookies, err := GetCookies()
	if err != nil {
		return
	}

	req.Header.Add("Cookie", cookies)
	req.Header.Add("Content-Type", "application/json")
	req.Header.Add("Accept", "application/json")

	resp, err = c.Do(req)
	if err != nil {
		return
	}
	if resp.StatusCode != http.StatusOK {
		err = fmt.Errorf("ERROR: request to %s return status code of %d", URL, resp.StatusCode)
		return
	}

	return
}

func RestGetAndUnmarshal(URL string, filters filters, start, limit uint, all bool, v any) (err error) {

	resp, err := RestGet(URL, filters, start, limit, all)
	if err != nil {
		return
	}
	defer resp.Body.Close()

	bytes, err := io.ReadAll(resp.Body)
	if err != nil {
		return
	}

	data := struct {
		Data any `json:"data"`
	}{
		Data: v,
	}

	err = json.Unmarshal(bytes, &data)
	if err != nil {
		return
	}

	return
}

func RestGetToFile(filename string, URL string, filters filters, start, limit uint, all bool) (err error) {

	resp, err := RestGet(URL, filters, start, limit, all)
	if err != nil {
		WriteToFile(filename, resp.Body)
		return
	}
	defer resp.Body.Close()

	_, err = WriteToFile(filename, resp.Body)
	if err != nil {
		return
	}

	return
}

func RestGET(URL string, filters filters, start, limit uint) (body []byte, err error) {

	form := url.Values{}
	form.Add("fields", "[\"*\"]")

	form.Add("filters", filters.String())
	form.Add("limit_start", fmt.Sprint(start))
	form.Add("limit_page_length", fmt.Sprint(limit))

	c := http.Client{}
	req, err := http.NewRequest("GET", URL+fmt.Sprint("?"+form.Encode()), nil)
	if err != nil {
		return
	}

	cookies, err := GetCookies()
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

	body, err = io.ReadAll(resp.Body)
	if err != nil {
		return
	}

	return
}
