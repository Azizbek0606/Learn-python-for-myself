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