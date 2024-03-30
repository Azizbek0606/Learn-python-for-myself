let url = "http://127.0.0.1:8000/api/category/"

function getCategory(html_element) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            for (let i = 0; i < data.length; i++) {
                let a = document.createElement('a');
                a.textContent = data[i].name;
                a.href = "/";
                html_element.appendChild(a);
            }
        })
}
let category_btn = document.querySelectorAll('.category_btn');
let category_list = document.querySelector('.category_list');
let categories_text_wrapper = document.querySelector('.categories_text_wrapper');
for (let i = 0; i < category_btn.length; i++) {
    category_btn[i].addEventListener('click', () => {
        while (categories_text_wrapper.firstChild) {
            categories_text_wrapper.removeChild(categories_text_wrapper.firstChild);
        }
        getCategory(categories_text_wrapper)
        category_list.classList.toggle('active_category_list');
    });
}
let search_block = document.querySelectorAll('.search_btn_nav');
for (let i = 0; i < search_block.length; i++) {
    search_block[i].addEventListener('click', () => {
        document.querySelector('.search_block').classList.toggle('active_search_block');
    });
}