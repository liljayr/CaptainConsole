let confirm_div = document.getElementById("delivery_info");
let card_div = document.getElementById("card_info")

for (let i=0; i<localStorage.length; i++) {
    let key = localStorage.key(i);
    if (key == "Cardholder" || key == "Cardnumber" || key == "Expiration date" || key == "CVC" && key != "cart") {
        card_div.innerHTML += "<p>" + key + ": " + localStorage.getItem(key) + "</p>"
    }
    else if (key != "cart"){
        confirm_div.innerHTML += "<p>" + key + ": " + localStorage.getItem(key) + "</p>"
    }

}


let clear_button = document.getElementById("confirm_button")
clear_button.onclick = function () {
    localStorage.clear()
}

