window.onload = (function () {
    let tags = document.getElementsByTagName("pre");
    for (var i = 0; i < tags.length; ++i) {
        tags[i].classList.add("prettyprint");
    }
    tags = document.getElementsByTagName("code");
    // console.log(tags);
    for (var i = 0; i < tags.length; ++i) {
        if (tags[i].classList.contains("language-python")) {
            tags[i].classList.add("lang-py");
            tags[i].classList.remove("language-python");
        }
        if (tags[i].classList.contains("language-err")) {
            tags[i].parentElement.classList.add("err");
            tags[i].parentElement.classList.remove("prettyprint");

        }
    }
    PR.prettyPrint();
})