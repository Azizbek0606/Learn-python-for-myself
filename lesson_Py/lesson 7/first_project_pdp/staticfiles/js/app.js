let url = ["http://127.0.0.1:8000/api/category/", "http://127.0.0.1:8000/api/tag/"]

function getCategory(html_element, into_url) {
    color_arr = ["#F38181", "#0F4C75", "#14FFEC", "#FCE38A"]
    color_name_arr = ["Red", "Blue", "Green", "Yellow"]
    fetch(into_url)
        .then(response => response.json())
        .then(data => {
            if (into_url != url[1]) {
                for (let i = 0; i < data.length; i++) {
                    let a = document.createElement('a');
                    a.textContent = data[i].name;
                    a.href = "/";
                    html_element.appendChild(a);
                }
            } else {
                for (let i = 0; i < data.length; i++) {
                    let main_block_tag = document.createElement('div');
                    main_block_tag.className = 'main_tag_block';
                    let a = document.createElement('a');
                    let circle = document.createElement('div');
                    let get_index = color_name_arr.indexOf(data[i].name);
                    let color = color_arr[get_index];
                    circle.style.cssText = `
                    width: 20px;
                    height: 20px;
                    background-color:${color};
                    border-radius: 100%;`
                    main_block_tag.append(circle);
                    main_block_tag.appendChild(a);
                    a.textContent = data[i].name;
                    a.style.color = color;
                    a.href = "/";
                    html_element.appendChild(main_block_tag);
                }
            }
        })
}




function get_category_tag(btn, list, wrapper_block, dynamic_url, class_name) {
    for (let i = 0; i < btn.length; i++) {
        btn[i].addEventListener('click', () => {
            while (wrapper_block.firstChild) {
                wrapper_block.removeChild(wrapper_block.firstChild);
            }
            getCategory(wrapper_block, dynamic_url)
            list.classList.toggle(class_name);
        });
    }
}

let category_btn = document.querySelectorAll('.category_btn');
let category_list = document.querySelector('.category_list');
let categories_text_wrapper = document.querySelector('.categories_text_wrapper');
get_category_tag(category_btn, category_list, categories_text_wrapper, url[0], "active_category_list")

let tag_btn = document.querySelectorAll('.tags_btn');
let tags_list = document.querySelector('.tags_list');
let tags_text_wrapper = document.querySelector('.tags_text_wrapper');
get_category_tag(tag_btn, tags_list, tags_text_wrapper, url[1], "active_tags_list")

let search_block = document.querySelectorAll('.search_btn_nav');
for (let i = 0; i < search_block.length; i++) {
    search_block[i].addEventListener('click', () => {
        document.querySelector('.search_block').classList.toggle('active_search_block');
    });
}
let image_blocks = document.querySelectorAll('.image_block');
for (let i = 0; i < image_blocks.length; i++) {
    image_blocks[i].style.cssText = `background-image: url(${image_blocks[i].getAttribute("this_block_image")});
    background-repeat: no-repeat;
    background-size: contain;
    background-position: center;`};


let card = document.querySelectorAll(".card");
let author = document.querySelectorAll(".author");

for (let i = 0; i < card.length; i++) {
    card[i].addEventListener('mouseover', () => {
        author[i].style.transform = "translate(5px)";
    });
    card[i].addEventListener('mouseout', () => {
        author[i].style.transform = "";
    });
}
