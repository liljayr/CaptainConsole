function displayInCheckout() {
        let cart_str = localStorage.getItem("cart");
        if (cart_str != null) {
            let cart = JSON.parse(cart_str);
            let item_count_div = document.getElementById("checkout_item_count");
            let header_div = document.getElementById("checkout_header");
            let items_div = document.getElementById("checkout_items");
            let separated_price_div = document.getElementById("separated_price");
            let total_price_div = document.getElementById("checkout_total");
            let total_price = 0;
            let total_amount = 0;

            for (let i = 0; i < cart.length; i++) {
                let product_info = cart[i].product_id.split("_");
                let name = product_info[2];
                let price = JSON.parse(product_info[3]);
                let amount = JSON.parse(cart[i].amount);
                total_amount += amount;
                total_price += price * amount;
                let total_price2 = total_price.toFixed(2);
                items_div.innerHTML += `<div class="checkout_single_item">
                                        <div class="item_checkout"><p>` + name + `</p></div>
                                        <div class="item_checkout"><p>` + amount + `</p></div>
                                        <div class="item_checkout"><p>$` + price + `</p></div>
                                        </div>`

                if (i == (cart.length) - 1) {
                    let total_price_plus_shipping = total_price + 10;
                    let total_price_plus_shipping2 = total_price_plus_shipping.toFixed(2);
                    separated_price_div.innerHTML += `<p>Subtotal: $` + total_price2 + `</p>
                                                     <p>Shipping: $` + 10.0 + `</p>`
                    total_price_div.innerHTML += `<div class="total_price">
                                                <p>Total price: $` + total_price_plus_shipping2 + `</p>
                                          </div>`
                    item_count_div.innerHTML += `<p>Items: `+ total_amount +`</p>`
                };
            };
        }

};

let checkout_button = document.getElementById("checkout_button");
checkout_button.onclick = function() {
    displayInCheckout();
    }
