.content {
    position: relative;
    display: block;
    top: 8em;
    width: 90%;
    margin-left: auto;
    margin-right: auto;
    padding:1em;
    padding-bottom:5.2em;
    -webkit-box-shadow:0 0 8px rgba(0,0,0,.8);
    -moz-box-shadow:0 0 8px rgba(0,0,0,.8);
    box-shadow: 0 0 8px rgba(0,0,0,.8);
}

footer {
    position: fixed;
    width: 90%;
    left:50%;
    margin: 0 0 0 -45%;
    bottom:0;
    padding:0.8em;
    -webkit-box-shadow:0 0 8px rgba(0,0,0,.8);
    -moz-box-shadow:0 0 8px rgba(0,0,0,.8);
    box-shadow: 0 0 8px rgba(0,0,0,.8);
    font-size: 0.8em;
    text-align:center;
    z-index:10;
    background:{{footer_background}};
}

h1, h2, h3, h4, h5, h6, p {
    font-family: 'Roboto', Helvtica, Arial;
    margin:0.5em;
}

h1 {
    font-size: 1.2em;
}

h2, h3, h4, h5, h6 {
    font-size: 1em;
}

p {
    font-family: 'Roboto', Helvtica, Arial;
    font-size: 0.8em;
}

 ul, li {
    font-family: 'Roboto', Helvtica, Arial;
    font-size: 0.8em;
}

li {
    margin:0.2em;
}

img {
    font-family: 'Roboto', Helvtica, Arial;
    font-size: 0.8em;
    width: 60%;
    -webkit-border-radius:0.5em;
    -moz-border-radius:0.5em;
    border-radius:0.5em;
}

.img-small {
    width: 20%;
}

.img-large {
    width: 80%;
}

.img-portfolio {
    width:100%;
    padding:0.7em;
    vertical-align: middle;
}

.img-modal {
    width: 90%;
}

.portfolio-container {
    display:inline-block;
    width: 150px;
    height: 150px;
    margin: 5px;
    line-height: 150px;
    text-align: center;
    -webkit-box-shadow:0 0 8px rgba(0,0,0,.8);
    -moz-box-shadow:0 0 8px rgba(0,0,0,.8);
    box-shadow: 0 0 8px rgba(0,0,0,.8);
    -webkit-border-radius:5px;
    -moz-border-radius:5px;
    border-radius:5px;
}

.portfolio-container:hover {
    background-color: rgba(0, 176, 240, 0.2);
}

.elevator-button:hover {
    text-decoration: underline;
}



.modalDialog {
    position: fixed;
    top: 5%;
    left: 0;
    font-family: 'Roboto', Helvtica, Arial;
    z-index: 99999;
    background: #000;
    opacity:0;
    -webkit-transition: opacity 400ms ease-in;
    -moz-transition: opacity 400ms ease-in;
    transition: opacity 400ms ease-in;
    pointer-events: none;
    width:100%;
    width:100vw;
    text-align:center;
    -webkit-box-shadow:0 0 8px rgba(0,0,0,.8);
    -moz-box-shadow:0 0 8px rgba(0,0,0,.8);
    box-shadow: 0 0 8px rgba(0,0,0,.8);
    -webkit-border-radius:5px;
    -moz-border-radius:5px;
    border-radius:5px;
    padding: 5%;
}

.modalDialog:target {
	opacity:1;
	pointer-events: auto;
}

.modalDialog > div {
	width: 100%;
	position: relative;
	margin-left:auto;
        margin-right:auto;
}
