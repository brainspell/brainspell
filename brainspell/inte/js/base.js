/*------------------------------------------------------------------------------
    JS Document (https://developer.mozilla.org/en/JavaScript)

    project:    Brain
    created:    2012-03-30
    author:     Christophe ANDRIEU (http://www.stpo.fr)

    summary:    CONSTANTES
                UTILITIES
                WINDOW.ONLOAD
                EASIN_CUSTOMZ
                ROLLOVER
                COLLAPSE
                EMAIL
                PLACEHOLDER
                PROFILE
                ADD-TAG
----------------------------------------------------------------------------- */
(function($) {

    /*  =CONSTANTES
    ----------------------------------------------------------------------------- */
    $.noConflict();
    var d = document;
    var w = window;
    stpo = {};


    /*  =UTILITIES
    ----------------------------------------------------------------------------- */
    var log = function(x) {
        if (typeof console != 'undefined') {
            console.log(x);
        }
    };


    /*  =WINDOW.ONLOAD
    ----------------------------------------------------------------------------- */
    $(document).ready(function(){

        // Call Functions
        stpo.rollMe();                  // image rollover
        stpo.placeholder();             // placeholder for input
        stpo.collapseMe();              // list collapse
        stpo.email();                   // email encode
        stpo.profile();                 // profile form behave
        stpo.add();                     // add tag to paper

        if ($.browser.msie && (($.browser.version == 6) || ($.browser.version == 7))){
            // IE 6-7 FUNCTIONS ONLY

        }

    });


    /*  =EASIN_CUSTOMZ
    ----------------------------------------------------------------------------- */
    $.extend( $.easing,{
        def: 'easeOutBounce',
        easeOutBounce: function (x, t, b, c, d) {
            if ((t/=d) < (1/2.75)) {
                return c*(7.5625*t*t) + b;
            } else if (t < (2/2.75)) {
                return c*(7.5625*(t-=(1.5/2.75))*t + .75) + b;
            } else if (t < (2.5/2.75)) {
                return c*(7.5625*(t-=(2.25/2.75))*t + .9375) + b;
            } else {
                return c*(7.5625*(t-=(2.625/2.75))*t + .984375) + b;
            }
        },
        easeOutExpo: function (x, t, b, c, d) {
            return (t==d) ? b+c : c * (-Math.pow(2, -10 * t/d) + 1) + b;
        }
    });


    /*  =ROLLOVER
    ----------------------------------------------------------------------------- */
    stpo.rollMe = function() {

        $('.rollMe').each(function(){

            var $myImg = $(this);

            // hover image preload
            var myHoverImg = document.createElement('img');
            myHoverImg.setAttribute("src", $myImg[0].src.slice(0,-4) + '_hover' + $myImg[0].src.substr($myImg[0].src.length - 4));

            // active image preload
            var myActiveImg = document.createElement('img');
            myActiveImg.setAttribute("src", $myImg[0].src.slice(0,-4) + '_active' + $myImg[0].src.substr($myImg[0].src.length - 4));

            // image rollover
            $(myHoverImg).load(function(){

                $myImg.parent('a, button').bind('mouseenter focus', function(){

                    if ($myImg[0].src.indexOf('_active') == -1)
                        $myImg[0].src = $myImg[0].src.slice(0,-4) + '_hover' + $myImg[0].src.substr($myImg[0].src.length - 4); // tricky IE substr bug

                }).bind('mouseleave blur', function(){
                    if ($myImg[0].src.split('_hover')[1])
                        $myImg[0].src = $myImg[0].src.split('_hover')[0] + $myImg[0].src.split('_hover')[1];

                });

            });

            // image click
            $(myActiveImg).load(function(){

                var doClick = true;

                // image mousedown
                $myImg.parent('a, button').bind('mousedown', function(){

                    if (doClick){
                        $myImg[0].src = $myImg[0].src.slice(0,-10) + '_active' + $myImg[0].src.substr($myImg[0].src.length - 4); // tricky IE substr bug
                        doClick = false;
                    }

                });

                // image mouseup
                $myImg.parent('a, button').bind('mouseup', function(){

                    if (!doClick){
                        $myImg[0].src = $myImg[0].src = $myImg[0].src.split('_active')[0] + '_hover' + $myImg[0].src.split('_active')[1];
                        doClick = true;
                    }

                });

            });

        });

    }


    /*  =COLLAPSE
    ----------------------------------------------------------------------------- */
    stpo.collapseMe = function(){

        $('.JS_collapse').each(function(){

            var $that = $(this),
                target = $that.attr('href');

            $that.bind('click',function(){

                if ($that.hasClass('closed')){

//                    $(target).slideDown('slow');
                    $(target)[0].style.display = 'block';
                    $that.removeClass('closed').html('-').attr('title','hide list');;

                }else{

//                    $(target).slideUp('slow');
                    $(target)[0].style.display = 'none';
                    $that.addClass('closed').html('+').attr('title','show list');

                }

                $that.blur();
                return false;

            });

        });

    }


    /*  =EMAIL
    ----------------------------------------------------------------------------- */
    stpo.email = function() {

        $('.email').each(function(i){

            var $that = $(this);
            var myString = $that.html();
            var newString = myString.split('[AT]')[0] + '@' + myString.split('[AT]')[1].split('[DOT]')[0] + '.' + myString.split('[AT]')[1].split('[DOT]')[1];

            if ($that.parent().hasClass('picto')){
                $that.html('<a href="mailto:' + newString + '" class="'+ $that.parent()[0].className +'">' + newString +'</a>');
                $that.parent().removeClass('picto');
            }
            else
                $that.html('<a href="mailto:' + newString + '">' + newString +'</a>');

        });

    };


    /*  =PLACEHOLDER
     ----------------------------------------------------------------------------- */
    stpo.placeholder = function(){

        $('input[type=text], input[type=search], input[type=password], input[type=email], textarea:not([readonly]').each(function(i){

            var $that = $(this);

            // placeHold me!
            if ($that.attr('value') == "") {
                $that.val($that.attr('title'));
                $that.addClass('placeholded');
            }

            // only for webkit
            $that.bind('mouseup', function(e){
                e.preventDefault();
            });

            $that.bind('focus', function(e){

                //if ($that.val() == $that.attr('title')){
                $that.select();
                $that.removeClass('placeholded');
                //}
            });

            $that.bind('blur', function(e){

                if ($that.val() != $that.attr('title')) $that.removeClass('placeholded');
                else $that.addClass('placeholded');

                // refill if empty
                if (!/[a-zA-Z0-9]/.test($that.val())) {
                    $that.val($that.attr('title'));
                    $that.addClass('placeholded');
                }

            });
        });
    };


    /*  =PROFILE
     ----------------------------------------------------------------------------- */
    stpo.profile = function(){

        $('.table-profile .edit-link').each(function(i){

            var $that = $(this),
                $target = $($that.attr('href'));

            $target.hide();

            $that.bind('click',function(){

                if ($target.hasClass('open')){

                    $target.hide().removeClass('open');

                }else{

                    $('.table-profile .open').hide().removeClass('open');
                    $target.show().addClass('open');
                }

                $that.blur();
                return false;

            })
        });
    };


    /*  =ADD-TAG
     ----------------------------------------------------------------------------- */
    stpo.add = function(){

        // rating
        $('.rate a').each(function(i){

            var $that = $(this),
                $ul = $that.parent().parent('ul'),
                $loader = $ul.parent('div').next('.now-loading');

            $that.bind('click',function(){

                $ul.addClass('rating');
                $loader[0].style.visibility = "visible";

                // AJAX & co
                // remettre $loader[0] à hidden quand c'est fini
                // virer la class 'rating' à $ul
                // incrémenter l'élément cliqué
                // interdire un nouveau clic (passer de a à span)

                return false;

            });

        });

        // adding
        $('.add-link').each(function(i){

            var $that = $(this),
                $target = $($that.attr('href')),
                $li = $target.parent('li'),
                $input = $target.find('input'),
                $cancel = $target.find('.cancel'),
                $loader = $target.find('.now-loading');

            $target.hide();

            $that.bind('click',function(){

                $that.hide();

                $('.open .new-tag').hide();
                $('.open .add-link').show();
                $('.item').removeClass('open');

                $target.show();
                $target.find('input').focus();
                $li.addClass('open');

                $that.blur();
                return false;

            });

            $cancel.bind('click', function(){

                $target.hide();
                $li.removeClass('open');
                $that.show();

                return false;

            });

            $target.bind('submit', function(){

                $loader[0].style.visibility = "visible";
                $input.attr('readonly',true);

                // AJAX & co
                // remettre $loader[0] à hidden quand c'est fini =)
                // ajouter un nouveau bouton + en dessous

                return false;

            });

        });
    };

})(jQuery);