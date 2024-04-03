// search , tags and categories methods is beginning
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
                    a.href = `http://127.0.0.1:8000/by/category/${i + 1}`;
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
                    a.href = `http://127.0.0.1:8000/by/tags/${i + 1}`;
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
// search , tags , categories menu methods was ended

// show article author name is beginning
let image_blocks = document.querySelectorAll('.image_block');
for (let i = 0; i < image_blocks.length; i++) {
    image_blocks[i].style.cssText = `background-image: url(${image_blocks[i].getAttribute("this_block_image")});
    background-repeat: no-repeat;
    background-size: contain;
    background-position: center;`
};

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
// show article author name was ended 


// go back buttons 
let path = window.location.pathname;

if (path != "/user/panel/") {
    document.querySelector('.btn_for_back').style.display = "block";
} else {
    document.querySelector('.btn_for_back').style.display = "none";
}
// go back button method was ended


// delete modal methods is beginning
let delete_modal_btn = document.querySelectorAll('.delete_modal_btn');
let delete_modal = document.querySelector(".delete_modal")
let delete_article_url = document.querySelector('.delete_article_url');
for (let i = 0; i < delete_modal_btn.length; i++) {
    delete_modal_btn[i].addEventListener('click', () => {
        delete_modal.classList.toggle('active_delete_modal')
        delete_article_url.href = `${delete_modal_btn[i].getAttribute("article_id")}`
    });
}
// delete modal methods was ended

// search method is beginning
let all_articles = [];
let isArticlesFetched = false;

function get_articles_title() {
    if (!isArticlesFetched) {
        fetch("http://127.0.0.1:8000/api/article/")
            .then(response => response.json())
            .then(data => {
                all_articles = data;
                isArticlesFetched = true;
            })
            .catch(error => console.error("Fetching articles failed:", error));
    }
}

let input = document.querySelector('input');
let result_block = document.querySelector('.result_block');

function addClickListenerToResults() {
    for (let i = 0; i < result_block.children.length; i++) {
        result_block.children[i].addEventListener("click", () => {
            input.value = result_block.children[i].firstChild.textContent;
            result_block.innerHTML = '';
        });
    }
}

input.addEventListener('input', (e) => {
    if (!isArticlesFetched) {
        get_articles_title();
    }
    let value = e.target.value.toLowerCase();
    result_block.innerHTML = '';

    if (value.length) {
        let result = all_articles.filter(article =>
            article.title.toLowerCase().includes(value) ||
            article.content.toLowerCase().includes(value)
        );
        result.forEach(article => {
            let p = document.createElement('p');
            let subtitle = document.createElement('h6');
            let result_wrapper = document.createElement('div');
            result_wrapper.className = 'result_wrapper';
            subtitle.className = 'subtitle_article_search';
            subtitle.textContent = article.content.split(' ').slice(0, 3);
            p.textContent = article.title.split(' ').slice(0, 3);
            result_wrapper.appendChild(p);
            result_wrapper.appendChild(subtitle);
            result_block.appendChild(result_wrapper);
        });
        addClickListenerToResults();
    }
});

// search method was ended

// comment from

document.querySelector(".add_comment > h3").addEventListener('click', () => {
    document.querySelector(".add_comment").classList.toggle('active_comment_block');
});
