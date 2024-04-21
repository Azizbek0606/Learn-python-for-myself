// tags and categories methods is beginning

let protocol = window.location.protocol;
let host = window.location.host;
let url = [`${protocol}//${host}/api/category/`, `${protocol}//${host}/api/tag/`]

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
                    a.href = `${protocol}//${host}/by/category/${data[i].id}`;
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
                    a.href = `${protocol}//${host}/by/tags/${data[i].id}`;
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
//  tags , categories menu methods was ended


// search method is beginning
let all_articles = [];
let isArticlesFetched = false;

function get_articles_title() {
    if (!isArticlesFetched) {
        fetch(`${protocol}//${host}/api/article/`)
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
            subtitle.textContent = article.content.split(' ').slice(0, 1);
            p.textContent = article.title.split(' ').slice(0, 1);
            result_wrapper.appendChild(p);
            result_wrapper.appendChild(subtitle);
            result_block.appendChild(result_wrapper);
        });
        addClickListenerToResults();
    }
});

// search method was ended