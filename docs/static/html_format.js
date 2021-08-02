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
        let br = document.createElement("br");
        while (tags[i].contains(br)) {
            console.log(tags[i], "true");
            tags[i].removeChild(br);
        }
    }
    PR.prettyPrint();
})