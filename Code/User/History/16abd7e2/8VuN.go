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

	// async.EnableAsync()
}

func getAsyncF(name string) async.AsyncF {
	return func() (err error) {

		f, err := types.GetFarm(name)
		if err != nil {
			return
		}

		err = f.GetPerformanceAppraisal()
		if err != nil {
			return
		}

		fmt.Println(f.FarmName, " => ", f.FarmMap)

		return
	}
}

func main() {

	fs, err := types.GetAllFarms()
	handelError(err)
	fmt.Println()

	return

	farms := []async.AsyncF{
		getAsyncF("Gamea"),
		getAsyncF("Mamdoh"),
		getAsyncF("Abo Zaaid"),
		getAsyncF("Rajab Mahmoud"),
		getAsyncF("Meter Shehata"),
		getAsyncF("Abo Mecky"),
		getAsyncF("Rajab Khalaf"),
		getAsyncF("Abd Al Motaleeb"),
		getAsyncF("Mohamed Abd Al Nasser"),
		getAsyncF("Zainb Hasan"),
		getAsyncF("Al Batety"),
		getAsyncF("Nadia Saleh"),
		getAsyncF("Al Maghraby 2"),
		getAsyncF("Khalaf allah al Baraeem"),
		getAsyncF("Abd Al Rady Mahmoud"),
		getAsyncF("Ahfad Abo Al Haroon"),
		getAsyncF("Muhamed Mostafa"),
		getAsyncF("Attyia Al Zahry"),
		getAsyncF("Shaban Shamaradan (Al Fashn 2)"),
		getAsyncF("Hamooda"),
		getAsyncF("Al Fayroz"),
		getAsyncF("Al Shahawy"),
		getAsyncF("المستقبل"),
		getAsyncF("Sales Abd Al Hamid Ahmed Al Gahlan"),
		getAsyncF("Osama Montser Mahmoud Mohamed"),
		getAsyncF("Hasan Mohamed obeed  Abd Al Fatah"),
		getAsyncF("Abo Al Fadl Mostafa Mahmoud Mohamed"),
		getAsyncF("Ahmed Mahmoud Mohamed Abd Al Monaem"),
		getAsyncF("Nemr Awad"),
		getAsyncF("Fawzy Abo al Wafaa"),
		getAsyncF("Ezz Al Den"),
		getAsyncF("Wasfy Moftah"),
		getAsyncF("Khair allah mousa"),
		getAsyncF("Abd Al Fatah Ismail"),
		getAsyncF("Ahmed Bakr Fathy Tahon"),
		getAsyncF("Talaaa 1"),
		getAsyncF("Ramadan Wahba"),
		getAsyncF("Ahmed Wahba"),
		getAsyncF("Mohamed Mahmoud Talaa"),
		getAsyncF("Mohamed Ali Mohamed khalifa"),
		getAsyncF("Nashaat Nan"),
		getAsyncF("Abd Allah Dweeb"),
		getAsyncF("Shehata"),
		getAsyncF("soliman"),
		getAsyncF("Mohamed Zidan"),
		getAsyncF("Saaleh"),
		getAsyncF("Abd Al Shafy Mohamed Maree Abd Al Rehim"),
		getAsyncF("Saed Sharakawy"),
		getAsyncF("Awlad Eker"),
		getAsyncF("Moursy Ali Al Herdaia"),
		getAsyncF("Abd Al Fatah Salamon"),
		getAsyncF("Amen Ahmed Rashwan"),
		getAsyncF("Abo Bakr Abo Al Fetouh Al Gredat"),
		getAsyncF("Sameh Khalaf Al Gredat"),
		getAsyncF("Ayaab Faheem Al Gredat"),
		getAsyncF("Mohamed Khalaf Al Gredat"),
		getAsyncF("Soliman Omran Al Gredat"),
		getAsyncF("Alaa Abdel Fattah Raslan"),
	}

	start := time.Now()

	defer func() {

		elapsed := time.Since(start)
		fmt.Printf("took %s\n", elapsed)
	}()

	err := async.RunAsync(farms...)
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
