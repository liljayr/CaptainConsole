function insertLocalStorage(button) {

        button.onclick = function () {
                let inputField = document.getElementById(button).value;
                if (inputField) {
                    localStorage.setItem("id", '4');
                }
            }
        location.reload();


};

let button = document.getElementById("view");
insertLocalStorage(button);

