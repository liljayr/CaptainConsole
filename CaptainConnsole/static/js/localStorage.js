
function insertLocalStorage(inputFields, buttons) {

    for (let i=0; i<buttons.length; i++) {
        buttons[i].onclick = function () {
            for (let j=0; j<inputFields.length; j++) {
                let inputField = document.getElementById(inputFields[j]).value;
                if (inputField) {
                    localStorage.setItem(inputFields[j], inputField);
                }
            }
        location.reload();
        };
    }
};

let inp_check = ["Country", "City", "Streetname", "Housenumber", "Postalcode", "Cardholder", "Cardnumber", "Expiration date", "CVC"];
let next_check = document.getElementById("next_button");
let back_check = document.getElementById("back_button");
let buttons_check = [next_check, back_check];

insertLocalStorage(inp_check, buttons_check);