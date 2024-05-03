const wrapper = document.querySelector('.blog_image_card_wrapper > div');
const wrapper1 = document.querySelector('.image_card_wrapper > div');
console.log(wrapper);
wrapper.addEventListener('wheel', function (e) {
    e.preventDefault();
    wrapper.scrollLeft += e.deltaY;
}, { passive: false });
wrapper1.addEventListener('wheel', function (e) {
    e.preventDefault();
    wrapper1.scrollLeft += e.deltaY;
}, { passive: false });


function tab_method_to_user_interface(element1 , element2 , btn , second) {
    element1.style.display = "none";
    element2.style.display = "block";
    btn.style.fontSize = '2em';
    second.style.fontSize = "1em"
}