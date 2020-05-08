(function () {
    let inpCountry = document.getElementById("country");
    let inpCity = document.getElementById("city");
    let inpStreetName = document.getElementById("streetname");
    let inpHouseNumber = document.getElementById("housenumber");
    let inpPostalCode = document.getElementById("postalcode");

    let inpCardholder = document.getElementById("cardholder");
    let inpCardnumber = document.getElementById("cardnumber");
    let inpExpirationDate = document.getElementById("expiration_date");
    let inpCVC = document.getElementById("cvc");

    let next = document.getElementById("next_button");
    let back = document.getElementById("back_button");


    let buttons = [next, back];
    for (let i=0; i<2; i++) {
        buttons[i].onclick = function () {
        let country = inpCountry.value;
        let city = inpCity.value;
        let streetname = inpStreetName.value;
        let housenumber = inpHouseNumber.value;
        let postalcode = inpPostalCode.value;
        let cardholder = inpCardholder.value;
        let cardnumber = inpCardnumber.value;
        let expiration_date = inpExpirationDate.value;
        let cvc = inpCVC.value;
        if (country) {
            localStorage.setItem("Country",country);
        }
        if (city) {
            localStorage.setItem("City", city);
        }
        if (streetname) {
            localStorage.setItem("Streetname", streetname);
        }
        if (housenumber) {
            localStorage.setItem("Housenumber", housenumber);
        }
        if (postalcode) {
            localStorage.setItem("Postalcode", postalcode);
        }
        if (cardholder){
            localStorage.setItem("Cardholder", cardholder);
        }
        if (cardnumber){
            localStorage.setItem("Cardnumber", cardnumber);
        }
        if (expiration_date){
            localStorage.setItem("Expiration date", expiration_date);
        }
        if (cvc){
            localStorage.setItem("CVC", cvc);
        }
        location.reload();

        };
    }



    })();

