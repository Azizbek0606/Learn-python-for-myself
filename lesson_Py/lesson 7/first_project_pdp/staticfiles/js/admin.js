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