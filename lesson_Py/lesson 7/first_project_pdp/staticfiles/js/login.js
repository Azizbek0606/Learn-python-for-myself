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
const url = "http://172.20.10.3:322/api/users/";

async function fetchUsernames(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        return data.map(user => user.username);
    } catch (error) {
        console.error('Error:', error);
        return [];
    }
}

let usernamesList = [];

fetchUsernames(url).then(usernames => {
    usernamesList = usernames.map(username => username.toLowerCase());
    console.log(usernamesList);

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
                    <span>User name is already taken</span>
                </p>`;
            } else {
                check_user_name[index].innerHTML = `<p class="check_user_name good_user_name">
                    <span class="icon_wrapper_user_name true_icon"><i class="fa-solid fa-check"></i></span>
                    <span>User name is available</span>
                </p>`;
            }
        });
    });
}).catch(error => {
    console.error("Failed to load usernames:", error);
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


function check_form(button, ...fields) {
    const minLengths = [6, 8, 5, 5];
    const isSignup = fields.length === 4;

    if (isSignup && fields[2] !== fields[3]) {
        alert('Passwords do not match!');
        return;
    }

    const allValid = fields.every((field, index) => field.trim().length >= minLengths[index % minLengths.length]);

    if (!allValid) {
        tempMessage(button, 'something worng or too short', 2000);
        return;
    }

    button.disabled = true;
    button.value = 'Sending…';
    button.form.submit();
}

function validateForm(button, ...args) {
    const allFilled = args.every(arg => arg.trim().length > 0);
    if (!allFilled) {
        tempMessage(button, 'Fill out the form', 2000);
        return;
    }
    check_form(button, ...args);
}

function tempMessage(element, message, duration) {
    const originalText = element.value;
    element.value = message;
    setTimeout(() => {
        element.value = originalText;
    }, duration);
}

