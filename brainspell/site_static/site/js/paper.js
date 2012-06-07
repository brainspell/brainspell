var CLASS_LIKE = 'like';
var CLASS_DISLIKE = 'dislike';
var AJAX_BASE_URL = "/ajax_";

jQuery(document).ready(function($) {

/*
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

*/

    $('ul.rate a').click(function() {
        if (!is_auth) {
            alert("You need to be authentified to submit tag ratings.");
            return false;
        }
        var link = $(this);
        if (link.hasClass(CLASS_LIKE)) {
            like(link);
        } else {
            dislike(link);
        };
    });


/*
    $('.task-list .new-tag input[name="label"]').each(function(){
        $(this).autocomplete({
            serviceUrl: '/ajax_autocomplete',
            params: {
                parent: $(this).attr('data-parent-id'),
                type: 'T',
            }
        });
    });

    $('.domain-list .new-tag input[name="label"]').each(function(){
        $(this).autocomplete({
            serviceUrl: '/ajax_autocomplete',
            params: {
                parent: $(this).attr('data-parent-id'),
                type: 'D',
            }
        });
    });
*/

    $('.new-tag select').change(function() {
        var textField = $(this).parent().find('.new-tag-free');
        var selected = $(this).find('option:selected').val();
        if (selected == 'other') {
            textField.show('fast', function() {
                textField.focus();
            });
        } else {
            textField.hide('fast');
        };
    });

});

function add_task() {

};

function add_domain() {

};

function _tag() {

};

function    like(link) { _rate(link, CLASS_LIKE);    };
function dislike(link) { _rate(link, CLASS_DISLIKE); };

function _rate(link, rating) {

    var tag_id = link.parents().eq(3).attr('data-tagid');   // --- The tag id is stored on an attribute of the link's 4th parent.
    var list = link.parent().parent('ul');
    var loader = list.parent('div').next('.now-loading');

    var url = AJAX_BASE_URL + rating;
    var feedback_id = '#' + rating + 's-' + tag_id;

    list.addClass('rating');
    loader[0].style.visibility = "visible";

    jQuery.post(url, {id: tag_id}, function(data){
        var feedback = JSON.parse(data);

        if(feedback['action_status'] == 1) {
            var feedback_data = feedback.raw_data[0].fields;
            var num_ratings = -1;
            switch(rating) {
                case CLASS_LIKE: {
                    num_ratings = feedback_data.num_likes;
                    break;
                };
                case CLASS_DISLIKE: {
                    num_ratings = feedback_data.num_dislikes;
                    break;
                };
            };
            jQuery(feedback_id).text(num_ratings);
        };

        list.removeClass('rating');
        loader[0].style.visibility = "hidden";

    });

};

