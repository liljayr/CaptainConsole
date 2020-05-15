let deliveryForm = document.getElementById("confirm-delivery-form");
let cardForm = document.getElementById("confirm-card-form")

function renderFormValue(label, value) {
  return `
    <div class="form-group">
        <label>${label}:</label>
        <span>${value}</span>
    </div>`;
}

function renderDeliveryInfo() {
    const deliveryInfo = JSON.parse(localStorage.getItem('delivery')) || {};
    const readableLabel = {
        "country": 'Country',
        "city": 'City',
        "street_name": 'Street Name',
        "house_nr": 'House Number',
        "postal_code": 'Postal Code',
    }
    Object.keys(deliveryInfo).forEach(key => {
        if(readableLabel[key]) {
            deliveryForm.innerHTML += renderFormValue(readableLabel[key], deliveryInfo[key]);
        }
    });
}

function renderCardInfo() {
    const cardInfo = JSON.parse(localStorage.getItem('card')) || {};
    const readableLabel = {
        "card_holder": 'Card Holder',
        "card_num": 'Card Number',
        "Exp_date": 'Expiration Date',
        "CVC": 'CVC',
    }
    Object.keys(cardInfo).forEach(key => {
        if(readableLabel[key]) {
            cardForm.innerHTML += renderFormValue(readableLabel[key], cardInfo[key]);
        }
    });
}

function AddToDB() {
    // ADD TO DB
    let cart = localStorage.getItem("cart");
    let hidden_cart = document.getElementById("hidden_cart");
    hidden_cart.value = cart;

    // CLEAR LOCALSTORAGE
    const confirmButton = document.getElementById("confirm_button");
    confirmButton.onclick = function () {
        window.localStorage.clear();
    };
}

AddToDB();

renderCardInfo();
renderDeliveryInfo();



