document.addEventListener("DOMContentLoaded", function () {
    //Login button event listener
    document.querySelector(".login-btn").addEventListener("click", function (event) {
        event.preventDefault();
        authenticateUser("/users/login/", "Login successful!", true);
    });

    //Creates account button event listener
    document.querySelector(".create-btn").addEventListener("click", function (event) {
        event.preventDefault();
        authenticateUser("/users/register/", "Account created! Please log in.");
    });

    function authenticateUser(url, successMessage, redirect = false) {
        //Gets username and password from input fields
        let username = document.querySelector("input[placeholder='Username']").value;
        let password = document.querySelector("input[placeholder='Password']").value;

        //Sends authentication request to Django backend
        fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username: username, password: password }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(successMessage);
                if (redirect) {
                    window.location.href = data.redirect;  //Redirects to chat if login succeeds
                }
            } else {
                alert("Error: " + data.error);
            }
        })
        .catch(error => console.error("Error:", error));
    }
});
