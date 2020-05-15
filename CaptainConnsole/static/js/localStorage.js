
function insertLocalStorage(inputFields, buttons) {
    for (let i=0; i<buttons.length; i++) {
        buttons[i].onclick = function () {
            for (let j=0; j<inputFields.length; j++) {
                let inputField = document.getElementById(inputFields[j]).val;
                if (inputField) {
                    localStorage.setItem(inputFields[j], inputField);
                };
            };
        };
    };
};






let inp_check = ["id_country", "id_city", "id_streetname", "id_housenr", "id_postal_code", "id_card_holder", "id_card_number", "id_Exp_date", "id_CVC"];
let next_check = document.getElementById("next_button");
let back_check = document.getElementById("back_button");
let buttons_check = [next_check, back_check];

insertLocalStorage(inp_check, buttons_check);