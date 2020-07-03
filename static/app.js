// change colour of output
function change_colour() {
    document.querySelector("#output").className = "blue-primary";
};

// loader appears in between pages and links
window.addEventListener("load", function () {
    const loaderWrap = document.querySelector(".loader-wrapper");
    loaderWrap.className += " hidden";
});

// loader appears after click button and waiting for flask to finish
function loading() {
    document.querySelector(".loader-wrapper").className = "loader-wrapper";
};

