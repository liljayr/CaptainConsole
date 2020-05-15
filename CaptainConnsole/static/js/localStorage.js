

function insertLocalStorage(key, fields) {
    const checkoutFields = {};
    fields.forEach(field => {
        let fieldValue = document.getElementById(`id_${field}`).value;
        if (fieldValue) {
            checkoutFields[field] = fieldValue;
        }
    })
    localStorage.setItem(key, JSON.stringify(checkoutFields));
}

$('#checkout-form').submit(() => {
    insertLocalStorage('delivery', checkout_fields);
})

$('#payment_form').submit(() => {
    insertLocalStorage('card', card_fields);
})


const checkout_fields = ["country", "city", "street_name", "house_nr", "postal_code"];
const card_fields = ["card_holder", "card_num", "Exp_date", "CVC"];

