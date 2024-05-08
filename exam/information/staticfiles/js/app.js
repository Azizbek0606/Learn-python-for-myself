window.addEventListener('scroll', function () {
    const navbar = document.querySelector('header');
    if (window.scrollY > 100) {
        navbar.style.cssText = `
    background: var(--card_gradient);
    border: 1px solid var(--secondary_opacity);
    border-radius: 20px;
    backdrop-filter: blur(var(--x-small-distance));`
    } else {
        navbar.style.cssText = `none`;
    }
});
function add_class_toggler(element, class_name) {
    element.classList.toggle(class_name);
}

let card = document.querySelectorAll('.card');
let dot = document.querySelectorAll('.class_for_set_attribute');
let color_list = ['#8e00f4', '#28ff33', '#7f0444', '#0A2342', '#1c5090', '#2196F3', '#6c49a4'];

function set_attributes_for_color(elements) {
    for (let i = 0; i < elements.length; i++) {
        let random_index = Math.floor(Math.random() * elements.length);
        elements[i].setAttribute('style', `--i: ${color_list[random_index]}`);
    }
}
set_attributes_for_color(card);
set_attributes_for_color(dot);