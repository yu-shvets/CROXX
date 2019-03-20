$('document').ready(function(){
    var update_q = $('.update_q');

    update_q.on('input', function(e){
        var form = $(this).parent('form');
        var id = form.attr('id').split('--')[1];
        console.log(id);

        $.ajax({
            url : form.attr('action'),
            type : "POST",
            data : form.serialize(),

            success: function(json){
                $('#sum--' + id).text(json.sum);
                $('.cart-sum').text(json.cart_sum);
            },
            error: function(e){
                console.log(e);
            }
        });

    });


});


$('.main-slider').slick({
  infinite: true,
  arrows: false,
});

$('.slider-for').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.slider-nav'
});
$('.slider-nav').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    asNavFor: '.slider-for',
    dots: false,
    arrows: true,
    focusOnSelect: true,
    centerMode: true,
    infinite: true,
    variableWidth: true,
    responsive: [
        {
            breakpoint: 1024,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
                infinite: true,
            }
        },
        {
            breakpoint: 600,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2
            }
        },
        {
            breakpoint: 480,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }
    ]

});


$('.delete').click(function() {
    console.log('here');
    $(this).closest('.product-item').remove();
});

$('.delete').click(function() {
    console.log('here');
    $(this).closest('.cart-product-item').remove();
});


// color-choose
$('.color-choose input').on('click', function() {
    var headphonesColor = $(this).attr('data-image');
    $('.active').fadeOut(500).removeClass('active');
    $('.left-column img[data-image = ' + headphonesColor + ']').fadeIn(250).addClass('active');
    $(this).addClass('active');
});





// numberSpinner

var numberSpinner = (function() {
    $('.number-spinner>.ns-btn>a').click(function() {
        var btn = $(this),
            oldValue = btn.closest('.number-spinner').find('input').val().trim(),
            newVal = 0;

        if (btn.attr('data-dir') === 'up') {
            newVal = parseInt(oldValue) + 1;
            console.log(oldValue);
        } else {
            if (oldValue > 1) {
                newVal = parseInt(oldValue) - 1;
                console.log(oldValue);
            } else {
                newVal = 1;
            }
        }
        btn.closest('.number-spinner').find('input').val(newVal);
    });
    $('.number-spinner>input').keypress(function(evt) {
        evt = (evt) ? evt : window.event;
        var charCode = (evt.which) ? evt.which : evt.keyCode;
        if (charCode > 31 && (charCode < 48 || charCode > 57)) {
            return false;
        }
        return true;
    });
})();



// Accordion

var accordion = (function (element) {

var _getItem = function (elements, className) {
var element = undefined;
elements.forEach(function (item) {
	if (item.classList.contains(className)) {
        element = item;
        }
 });
     return element;
};

return function () {
  var _mainElement = {},
    _items = {},
 _contents = {};

var _actionClick = function (e) {
    if (!e.target.classList.contains('accordion-item-header')) {
        return;
}
e.preventDefault();

var header = e.target,
item = header.parentElement,
itemActive = _getItem(_items, 'show');

if (itemActive === undefined) {
    item.classList.add('show');
} else {

itemActive.classList.remove('show');

 if (itemActive !== item) {

    item.classList.add('show');
		}
    }
},
_setupListeners = function () {

    _mainElement.addEventListener('click', _actionClick);
 };

return {
   init: function (element) {
    _mainElement = (typeof element === 'string' ? document.querySelector(element) : element);
    _items = _mainElement.querySelectorAll('.accordion-item');
    _setupListeners();
		}
    }
 }
 })();



var accordion1 = accordion();
accordion1.init('#accordion');











