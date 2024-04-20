let sign_up_toggle = document.querySelector(".sign_up");
let login_toggle = document.querySelector(".login_wrapper");
let form_wrapper = document.querySelector(".form_wrapper");
let btn_tab = document.querySelector(".btn_tab");
let check_user_name = document.querySelectorAll('.check_user_name');
let user_name_input = document.querySelectorAll('.user_name_input');
let login_sub_btn = document.querySelectorAll(".login_sub_btn");
let pas_input = document.querySelectorAll(".pas_input");
let progress_vizualization = document.querySelectorAll(".progress_vizualization");

function form_tab_method() {
    if (login_toggle.style.display === "none") {
        login_toggle.style.display = "block";
        sign_up_toggle.style.display = "none";
        form_wrapper.style.width = "450px";
        form_wrapper.style.height = "450px";
        btn_tab.textContent = "Sign up";
    } else {
        login_toggle.style.display = "none";
        sign_up_toggle.style.display = "block";
        form_wrapper.style.width = "800px";
        form_wrapper.style.height = "450px";
        btn_tab.textContent = "Login";
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
fetchUsernames(url);

user_name_input.forEach((input, index) => {
    input.addEventListener('input', function () {
        let values = input.value.replace(/ /g, "_").replace(" ", "_");
        input.value = values;
        if (values.length === 0) {
            check_user_name[index].innerHTML = `<p class="check_user_name">
                <span class="icon_wrapper_user_name"><i class="fa-solid fa-pen"></i></span>
                <span>Write your user name</span>
            </p>`;
        } else if (usernamesList.includes(values.toLowerCase())) {
            check_user_name[index].innerHTML = `<p class="check_user_name taken">
                <span class="icon_wrapper_user_name wrong_icon"><i class="fa-solid fa-xmark"></i></span>
                <span>user name</span>
                <span>is already taken</span>
            </p>`;
        } else {
            check_user_name[index].innerHTML = `<p class="check_user_name good_user_name">
                <span class="icon_wrapper_user_name true_icon"><i class="fa-solid fa-check"></i></span>
                <span>user name</span>
                <span>is available</span>
            </p>`;
        }
    });
});

pas_input.forEach((input, index) => {
    input.addEventListener("input", () => {
        let counter = 0;
        let progress_bar = progress_vizualization[index];
        if (input.value.length > 0) {
            progress_bar.parentElement.style.opacity = 1;
        } else {
            progress_bar.parentElement.style.opacity = 0;
        }

        if (input.value.length > 6) {
            if (/[!@#$%^&*()_+=\[\]{};':"\\|,.<>\/?]/.test(input.value)) {
                counter += 20;
            }
            if (/[0-9]/.test(input.value)) {
                counter += 20;
            }
            if (/[a-z]/.test(input.value)) {
                counter += 20;
            }
            if (/[A-Z]/.test(input.value)) {
                counter += 20;
            }
            if (input.value.length > 12) {
                counter += 20;
            }
        }

        progress_bar.style.width = counter + "%";
        if (counter < 40) {
            progress_bar.style.background = "linear-gradient(to right, #ff1e56, #ffac41)";
        } else if (counter < 80) {
            progress_bar.style.background = "linear-gradient(to right, #ffac41, #fffa90)";
        } else {
            progress_bar.style.background = "linear-gradient(to right, #69f0ae, #00e676)";
        }
    });
});

function check_form(button, username, password) {
    if (username.length >= 5 && password.length >= 5) {
        button.disabled = true;  // Faqat muvaffaqiyatli yuborishda tugmani o'chirish
        button.value = 'Sending…';
        button.form.submit();
    } else {
        button.disabled = false;  // Agar xatolik bo'lsa, tugmani qayta faollashtirish
        button.value = 'min length 5 | Submit';
    }
}
function check_form(button, username, email, password, confirm_password) {
    // Formani yuborish tugmachasini dastlabki holatiga qaytarish
    button.disabled = false;
    button.value = 'Submit';

    // Barcha shartlar bajarilganmi tekshirish
    if (username.length >= 6 && email.length >= 5 && password.length >= 5 && confirm_password.length >= 5) {
        if (password === confirm_password) {
            button.disabled = true;  // Tugmani o'chirish
            button.value = 'Sending…'; // Yuborish jarayonida tugmani matnini o'zgartirish
            button.form.submit(); // Formani yuborish
        } else {
            alert('Passwords do not match!'); // Parollar mos kelmasa ogohlantirish
        }
    } else {
        button.value = 'Fill correctly | Submit'; // To'ldirishda xatolik bo'lsa tugmani matnini o'zgartirish
    }
}