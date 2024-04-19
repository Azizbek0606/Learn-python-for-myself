let sign_up_toggle = document.querySelector(".sign_up");
let login_toggle = document.querySelector(".login_wrapper");
let form_wrapper = document.querySelector(".form_wrapper");
let btn_tab = document.querySelector(".btn_tab");
let check_user_name = document.querySelectorAll('.check_user_name')
let user_name_input = document.querySelectorAll('.user_name_input');
let login_sub_btn = document.querySelector(".login_sub_btn")
let pas_input = document.querySelectorAll(".pas_input");
let progress_vizualization = document.querySelectorAll(".progress_vizualization");
function form_tab_method() {
    if (login_toggle.style.display == "none") {
        login_toggle.style.display = "block";
        sign_up_toggle.style.display = "none";
        form_wrapper.style.width = "450px";
        form_wrapper.style.height = "450px";
        btn_tab.textContent = "Sign up"
    } else {
        login_toggle.style.display = "none";
        sign_up_toggle.style.display = "block";
        form_wrapper.style.width = "800px";
        form_wrapper.style.height = "450px";
        btn_tab.textContent = "Login"
    }
}
const url = "http://127.0.0.1:8000/api/users/";
let usernamesList = [];

function fetchUsernames(url) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            usernamesList = data.map(user => user.username);
        })
        .catch(error => console.error('Error:', error));
}

let already_taken = `<p class="check_user_name taken">
    <span class="icon_wrapper_user_name wrong_icon"><i class="fa-solid fa-xmark" ></i></span>
    <span>user name</span>
    <span>is already taken</span>
</p>`
let good_user_name = `<p class="check_user_name good_user_name">
    <span class="icon_wrapper_user_name true_icon"><i class="fa-solid fa-check"></i></span>
    <span>user name</span>
    <span>is available</span>
</p>`
let empty_input = `<p class="check_user_name">
    <span class="icon_wrapper_user_name"><i class="fa-solid fa-pen"></i></span>
    <span>Write your user name</span>
</p>`
function inducator_for_usernames(elements, user_name_list, url, values) {
    if (user_name_list.length > 0) {
        for (let i = 0; i < user_name_list.length; i++) {
            if (user_name_list[i].toLowerCase() === values.toLowerCase()) {
                elements.innerHTML = already_taken;
            } else if (values.length == 0) {
                elements.innerHTML = empty_input;
            } else {
                elements.innerHTML = good_user_name;
            }
        }
    }
    else {
        fetchUsernames(url);
    }
}

user_name_input.addEventListener('input', function (e) {
    let values = user_name_input.value.replace(/ /g, "_").replace(" ", "_");
    user_name_input.value = values;
    user_name_input.value = values;
    inducator_for_usernames(check_user_name, usernamesList, url, values);
    if (values.length > 5) {
        login_sub_btn.disabled = false;
        login_sub_btn.value = "Submit";
    } else {
        login_sub_btn.disabled = true;
        login_sub_btn.value = "min length 5 | Submit";
    }
});
let counter = 0;

pas_input.addEventListener("input", (e) => {
    counter = 0;

    if (pas_input.value.length > 0) {
        progress_vizualization.parentElement.style.opacity = 1;
    } else {
        progress_vizualization.parentElement.style.opacity = 0;
    }

    if (pas_input.value.length > 6) {
        if (/[!@#$%^&*()_+=\[\]{};':"\\|,.<>\/?]/.test(pas_input.value)) {
            counter += 20;
        }
        if (/[0-9]/.test(pas_input.value)) {
            counter += 20;
        }
        if (/[a-z]/.test(pas_input.value)) {
            counter += 20;
        }
        if (/[A-Z]/.test(pas_input.value)) {
            counter += 20;
        }
        if (pas_input.value.length > 12) {
            counter += 20;
        }
    }

    progress_vizualization.style.width = counter + "%";
    if (counter < 40) {
        progress_vizualization.style.background = "linear-gradient(to right, #ff1e56, #ffac41)";
    } else if (counter < 80) {
        progress_vizualization.style.background = "linear-gradient(to right, #ffac41, #fffa90)";
    } else {
        progress_vizualization.style.background = "linear-gradient(to right, #69f0ae, #00e676)";
    }


    if (pas_input.value.length > 14) {
        progress_vizualization.style.boxShadow = "0 0 10px 2px green";
    } else {
        progress_vizualization.style.boxShadow = "none";
    }
});