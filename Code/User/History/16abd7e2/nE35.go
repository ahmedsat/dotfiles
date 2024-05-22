package main

import (
	"fmt"
	"os"
	"time"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"github.com/ahmedsat/erp-reports/async"
	"github.com/ahmedsat/erp-reports/methods"
	"github.com/ahmedsat/erp-reports/screens"
	"github.com/ahmedsat/erp-reports/types"
)

// todo: farm structure
// todo: farm map

func handelError(err error) {
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
func init() {

	user, err := methods.GetAuthorizedUser()
	if err != nil {
		err := methods.Login("ahmedsat303@gmail.com", "123456789")
		handelError(err)
		user, err = methods.GetAuthorizedUser()
		handelError(err)
	}
	fmt.Println(user)

	async.EnableAsync()
}

func main() {

	start := time.Now()
	defer func() {
		elapsed := time.Since(start)
		fmt.Printf("\ntook %s\n", elapsed)
	}()

	farms, err := types.GetAllFarms()
	handelError(err)

	async.LogPresentSetMax("f", uint(len(farms)))

	functions := []async.AsyncF{}
	for i := range farms {
		functions = append(functions, farms[i].GetPerformanceAppraisal)
	}

	err = async.RunAsync(functions...)
	handelError(err)

}

func UI() {

	// dark mode doesn't work by default under wine for some reason
	// so this is work around to make it work
	os.Setenv("FYNE_THEME", "dark")

	myApp := app.New()
	w := myApp.NewWindow("Test")

	w.Canvas().SetOnTypedKey(func(ke *fyne.KeyEvent) {
		if ke.Name == fyne.KeyEscape {
			w.Close()
		}
	})

	screens.Home(w)
	w.ShowAndRun()

}
