package types

import (
	"encoding/json"
	"io"

	"github.com/ahmedsat/erp-reports/async"
	"github.com/ahmedsat/erp-reports/utils"
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
	IsPlotOfSector      int     `json:"is_plot_of_sector"`
	ArabicName          string  `json:"arabic_name"`
	UpscalingProject    string  `json:"upscaling_project"`
	Region              string  `json:"region"`
	ParentFarm          string  `json:"parent_farm"`
	Category            string  `json:"gategory"`
	FarmName            string  `json:"farm_name"`
	FarmAreaFeddan      float64 `json:"farm_area__feddan"`
	IsInternal          int     `json:"is_internal_farm"`
	Company             string  `json:"company"`
	FarmStatus          string  `json:"farm_status"`
	FarmId              string  `json:"farm_id"`
	RegisteredDate      string  `json:"registered_date"`
	FarmOwner           string  `json:"farm_owner"`
	FarmOwnership       string  `json:"farm_ownership"`
	FarmOperator        string  `json:"farm_operator"`
	Phone               string  `json:"phone"`
	Engineer            string  `json:"engineer"`
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

	// Farmers []Farmer `json:"farmers"` TODO: to be implemented

	FertilizationRecords              []FertilizationRecord
	SowingRecords                     []SowingRecord
	IrrigationRecords                 []IrrigationRecord
	FarmOperationsRecords             []FarmOperationsRecord
	ControlRecords                    []ControlRecord
	HarvestRecords                    []HarvestRecord
	TransportationAndReceivingRecords []TransportationAndReceivingRecord

	CompostingRecords []CompostingRecord

	FarmHedgeRecords      []FarmHedgeRecord
	SoilAndClimateRecords []SoilAndClimateRecord
	FeedingRecords        []FeedingRecord

	CropsPlanRecords []CropsPlanRecord

	FarmStructure bool
	FarmMap       bool
}

func GetFarm(name string) (farm *Farm, err error) {

	URL := "https://erp.sekem.com:86/api/resource/Farm/" + name

	filters := utils.NewFilters("Farm")

	filters.Add("type", "=", "Farm")

	farm = &Farm{}
	err = utils.RestGetAndUnmarshal(URL, filters, 0, 1, false, farm)
	if err != nil {
		return
	}

	return
}

func GetAllFarms() (farms []Farm, err error) {

	URL := "https://erp.sekem.com:86/api/resource/Farm/"

	filters := utils.NewFilters("Farm")
	filters.Add("type", "=", "Farm")

	// data := struct {
	// 	Data []Farm `json:"data"`
	// }{
	// 	Data: farms,
	// }

	utils.RestGetAndUnmarshalMany(URL, filters, 0, 1, false, farms)

	return
}

func (f *Farm) UpdateFarm() (err error) {
	URL := "https://erp.sekem.com:86/api/resource/Farm/" + f.Name

	filters := utils.NewFilters("Farm")

	filters.Add("type", "=", "Farm")

	err = utils.RestGetAndUnmarshal(URL, filters, 0, 1, true, f)
	if err != nil {
		return
	}

	return
}

func (f Farm) UpdateBaseRecords(record string) (records []BaseRecord, err error) {

	URL := "https://erp.sekem.com:86/api/resource/" + record
	filters := utils.NewFilters(record)
	filters.Add("farm", "=", f.Name)

	res, err := utils.RestGet(URL, filters, 0, 0, true)
	if err != nil {
		return
	}
	defer res.Body.Close()

	bytes, err := io.ReadAll(res.Body)

	data := struct {
		Data []BaseRecord `json:"data"`
	}{
		Data: []BaseRecord{},
	}

	err = json.Unmarshal(bytes, &data)
	if err != nil {
		return
	}

	records = data.Data

	return
}

func (f *Farm) UpdateCompostingRecords() (err error) {

	recs, err := f.UpdateBaseRecords("Composting Record")
	if err != nil {
		return
	}

	f.CompostingRecords = []CompostingRecord{}
	for _, rec := range recs {
		f.CompostingRecords = append(f.CompostingRecords, CompostingRecord{
			BaseRecord: rec,
		},
		)
	}

	return
}

func (f *Farm) UpdateFertilizationRecords() (err error) {

	recs, err := f.UpdateBaseRecords("Fertilization Record")
	if err != nil {
		return
	}

	f.FertilizationRecords = []FertilizationRecord{}
	for _, rec := range recs {
		f.FertilizationRecords = append(f.FertilizationRecords, FertilizationRecord{
			BaseRecord: rec,
		},
		)
	}
	return
}

func (f *Farm) UpdateSowingRecords() (err error) {

	recs, err := f.UpdateBaseRecords("Sowing Record")
	if err != nil {
		return
	}

	f.SowingRecords = []SowingRecord{}
	for _, rec := range recs {
		f.SowingRecords = append(f.SowingRecords, SowingRecord{
			BaseRecord: rec,
		},
		)
	}

	return
}

func (f *Farm) UpdateIrrigationRecords() (err error) {

	recs, err := f.UpdateBaseRecords("Irrigation Record")
	if err != nil {
		return
	}

	f.IrrigationRecords = []IrrigationRecord{}
	for _, rec := range recs {
		f.IrrigationRecords = append(f.IrrigationRecords, IrrigationRecord{
			BaseRecord: rec,
		},
		)
	}

	return
}

func (f *Farm) UpdateFarmOperationsRecords() (err error) {

	recs, err := f.UpdateBaseRecords("Farm Operations Record")
	if err != nil {
		return
	}

	f.FarmOperationsRecords = []FarmOperationsRecord{}
	for _, rec := range recs {
		f.FarmOperationsRecords = append(f.FarmOperationsRecords, FarmOperationsRecord{
			BaseRecord: rec,
		},
		)
	}

	return
}

func (f *Farm) GetControlRecords() (err error) {

	recs, err := f.UpdateBaseRecords("Control Record")
	if err != nil {
		return
	}

	f.ControlRecords = []ControlRecord{}
	for _, rec := range recs {
		f.ControlRecords = append(f.ControlRecords, ControlRecord{
			BaseRecord: rec,
		},
		)
	}

	return
}

func (f *Farm) UpdateHarvestRecords() (err error) {

	recs, err := f.UpdateBaseRecords("Harvest Record")
	if err != nil {
		return
	}

	f.HarvestRecords = []HarvestRecord{}
	for _, rec := range recs {
		f.HarvestRecords = append(f.HarvestRecords, HarvestRecord{
			BaseRecord: rec,
		},
		)
	}

	return
}

func (f *Farm) UpdateTransportationAndReceivingRecords() (err error) {

	recs, err := f.UpdateBaseRecords("Transportation and Receiving Record")
	if err != nil {
		return
	}

	f.TransportationAndReceivingRecords = []TransportationAndReceivingRecord{}
	for _, rec := range recs {
		f.TransportationAndReceivingRecords = append(f.TransportationAndReceivingRecords, TransportationAndReceivingRecord{
			BaseRecord: rec,
		},
		)
	}

	return
}

func (f *Farm) UpdateFarmHedgeRecords() (err error) {

	record := "Farm Hedge"
	URL := "https://erp.sekem.com:86/api/resource/" + record
	filters := utils.NewFilters(record)
	filters.Add("farm", "=", f.Name)

	res, err := utils.RestGet(URL, filters, 0, 0, true)
	if err != nil {
		return
	}
	defer res.Body.Close()

	bytes, err := io.ReadAll(res.Body)

	data := struct {
		Data []FarmHedgeRecord `json:"data"`
	}{
		Data: []FarmHedgeRecord{},
	}

	err = json.Unmarshal(bytes, &data)
	if err != nil {
		return
	}

	f.FarmHedgeRecords = data.Data

	return
}

func (f *Farm) UpdateSoilAndClimateRecords() (err error) {
	record := "Soil and Climate"
	URL := "https://erp.sekem.com:86/api/resource/" + record
	filters := utils.NewFilters(record)
	filters.Add("farm", "=", f.Name)

	res, err := utils.RestGet(URL, filters, 0, 0, true)
	if err != nil {
		return
	}
	defer res.Body.Close()

	bytes, err := io.ReadAll(res.Body)

	data := struct {
		Data []SoilAndClimateRecord `json:"data"`
	}{
		Data: []SoilAndClimateRecord{},
	}

	err = json.Unmarshal(bytes, &data)
	if err != nil {
		return
	}

	f.SoilAndClimateRecords = data.Data

	return
}

func (f *Farm) UpdateFeedingRecords() (err error) {

	recs, err := f.UpdateBaseRecords("Feeding Record")
	if err != nil {
		return
	}

	f.FeedingRecords = []FeedingRecord{}
	for _, rec := range recs {
		f.FeedingRecords = append(f.FeedingRecords, FeedingRecord{
			BaseRecord: rec,
		},
		)
	}

	return
}

func (f *Farm) UpdateCropsPlanRecords() (err error) {

	record := "Crops Plan"
	URL := "https://erp.sekem.com:86/api/resource/" + record
	filters := utils.NewFilters(record)
	filters.Add("farm", "=", f.Name)

	res, err := utils.RestGet(URL, filters, 0, 0, true)
	if err != nil {
		return
	}
	defer res.Body.Close()

	bytes, err := io.ReadAll(res.Body)

	data := struct {
		Data []CropsPlanRecord `json:"data"`
	}{
		Data: []CropsPlanRecord{},
	}

	err = json.Unmarshal(bytes, &data)
	if err != nil {
		return
	}

	f.CropsPlanRecords = data.Data

	return
}

func (f *Farm) GetPerformanceAppraisal() (err error) {

	err = f.UpdateFarm()
	if err != nil {
		return
	}

	funcs := []async.AsyncF{
		f.UpdateFertilizationRecords,
		f.UpdateSowingRecords,
		f.UpdateIrrigationRecords,
		f.UpdateFarmOperationsRecords,
		f.GetControlRecords,
		f.UpdateHarvestRecords,
		f.UpdateTransportationAndReceivingRecords,
		f.UpdateCompostingRecords,
		f.UpdateFarmHedgeRecords,
		f.UpdateSoilAndClimateRecords,
		f.UpdateFeedingRecords,
		f.UpdateCropsPlanRecords,
		f.UpdateFarmStructure,
		f.UpdateFarmMap,
	}

	err = async.RunAsync(funcs...)

	return
}
