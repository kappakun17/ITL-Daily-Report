/ JavaScript source code 

//rollAnime��roll�Ƃ����N���X����t�����` 

function RollAnimeControl() {

    $('.rollAnime').each(function () {

        var elemPos = $(this).offset().top - 50;

        var scroll = $(window).scrollTop();

        var windowHeight = $(window).height();

        var childs = $(this).children();  //rollAnime�̎q�v�f���擾 

        if (scroll >= elemPos - windowHeight) {

            $(childs).each(function (i) {   //�q�v�f��1��1�����������Ȃ� 

                if (i < 10) {         //10�����̏ꍇ 

                    $(this).css("transition-delay", "." + i + "s");  //�q�v�f��csstransition-delay��ǉ� 

                } else {             //10�ȏ�̏ꍇ 

                    var n = i / 10;       //�~���b�w��Ȃ̂�10�Ŋ��� 

                    $(this).css("transition-delay", n + "s");  //�q�v�f��csstransition-delay��ǉ� 

                }

            });



            $(this).addClass("roll"); //roll�Ƃ����A�j���[�V�����N���X��t�^ 



        } else {

            $(childs).each(function () {    //�q�v�f��1��1�����������Ȃ� 

                $(this).css("transition-delay", "0s");//�q�v�f��csstransition-delay�̕b��0�Ƃ��� 

            });

            $(this).removeClass("roll");//roll�Ƃ����A�j���[�V�����N���X������ 

        }

    });

}