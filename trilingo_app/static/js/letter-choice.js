const kzEmoji = document.querySelector('.langs-nav-item:nth-child(1) .emoji-sm');
const ruEmoji = document.querySelector('.langs-nav-item:nth-child(2) .emoji-sm');
const enEmoji = document.querySelector('.langs-nav-item:nth-child(3) .emoji-sm');

const kzLetter = document.querySelector('#kz');
const ruLetter = document.querySelector('#ru');
const enLetter = document.querySelector('#en');

function clearBorderBottom() {
  kzLetter.style.border = 'none';
  ruLetter.style.border = 'none';
  enLetter.style.border = 'none';
}

kzEmoji.addEventListener('click', function() {
  clearBorderBottom();
  kzLetter.style.marginTop = "10px";
  kzLetter.style.borderRadius = "10px";

  kzLetter.style.border = '2px solid #21428a';
});

ruEmoji.addEventListener('click', function() {
  clearBorderBottom();
  ruLetter.style.marginTop = "10px";
  ruLetter.style.borderRadius = "10px";

  ruLetter.style.border = '2px solid #21428a';
});

enEmoji.addEventListener('click', function() {
  clearBorderBottom();
  enLetter.style.marginTop = "10px";
  enLetter.style.borderRadius = "10px";
  enLetter.style.border = '2px solid #21428a';
});