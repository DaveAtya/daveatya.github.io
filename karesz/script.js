let kigyok = document.querySelector('#grid');
let kivalasztott = 'fal'
let szin = 'red'
let pigyok = document.querySelector('#butkaresz');
pigyok.addEventListener('click', () => {
    kivalasztott = 'karesz'
})
let rigyok = document.querySelector('#butfal');
rigyok.addEventListener('click', () => {
    kivalasztott = 'fal'
})
let migyok = document.querySelectorAll('.butkavics');
for (const migyo of migyok) {
    migyo.addEventListener('click', () => {
        kivalasztott = 'kavics'
        szin = migyo.getAttribute('data-color')
    })
}

for (let i = 0; i < 20 * 30; i++) {
    const box = document.createElement("div");
    kigyok.appendChild(box);
    box.classList.add('asd')
    box.addEventListener('click', () => {
        if (kivalasztott == 'kavics') {
            box.setAttribute('data-color', szin)
        }
        if (box.classList.contains(kivalasztott)) {
            box.className = 'asd'

        }
        else {
            box.className = 'asd'
            box.classList.toggle(kivalasztott)

        }

    })
}

