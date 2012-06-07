<?php include('inc/head.inc.php'); ?>

<body>

<?php include('inc/top-nav.logged.inc.php'); ?>

<div class="content-section">

    <?php include('inc/header.inc.php'); ?>

    <div id="core">

        <div class="content">

            <div class="section">

                <div class="clearfix">
                    <h2><strong>Help us</strong>  tagging these articles. <strong>Select</strong> a document below to
                        <strong>label it!</strong></h2>
                    <a href="#" class="fr refresh-link"><span>Refresh the list!</span></a>
                </div>

                <ul class="paper-list">
                    <li>
                        <div class="paper-stuff">
                            <h3><a href="#">Lorem Ipsum Sit Amet</a></h3>
                            <p class="info"><strong>Robert E. Neuman</strong> (2012) <strong>Neuroscience Magazine</strong> 35(4):50–57</p>
                        </div>
                        <a class="button" href="#">Please label me!</a>
                    </li>
                    <li>
                        <div class="paper-stuff">
                            <h3><a href="#">Regional cerebral blood flow abnormalities in depressed patients with cognitive impairment</a></h3>
                            <p class="info"><strong>Robert E. Neuman</strong> (2012) <strong>Neuroscience Magazine</strong> 35(4):50–57</p>
                        </div>
                        <a class="button" href="#">Please label me!</a>
                    </li>
                    <li>
                        <div class="paper-stuff">
                            <h3><a href="#">Lorem Ipsum Sit Amet Regional cerebral</a></h3>
                            <p class="info"><strong>Beauregard M, Gold D, Evans A C, Chertkow H</strong> (2012) <strong>Neuroscience Magazine</strong> 35(4):50–57</p>
                        </div>
                        <a class="button" href="#">Please label me!</a>
                    </li>
                    <li>
                        <div class="paper-stuff">
                            <h3><a href="#">Regional cerebral blood flow abnormalities in depressed patients with cognitive impairment</a></h3>
                            <p class="info"><strong>Robert E. Neuman</strong> in <strong>Neuroscience Magazine</strong> on <strong>01/01/2012</strong></p>
                        </div>
                        <a class="button" href="#">Please label me!</a>
                    </li>
                    <li>
                        <div class="paper-stuff">
                            <h3><a href="#">Regional cerebral blood flow abnormalities in depressed patients with cognitive impairment</a></h3>
                            <p class="info"><strong>Robert E. Neuman</strong> in <strong>Neuroscience Magazine</strong> on <strong>01/01/2012</strong></p>
                        </div>
                        <a class="button" href="#">Please label me!</a>
                    </li>
                </ul>

            </div><!-- /section -->

        </div><!-- /content -->

    </div><!-- /content-section -->

    <div class="content-section second-one clearfix">

        <div class="content">

            <form action="#">
                <fieldset class="section" id="home-search">
                    <h2><label for="search">Browse our database</label></h2>
                    <input type="text" id="search" title="Title, author, publication, Pubmed ID…">
                    <button><img src="img/bt_search.png" width="25" height="25" alt="Search" class="rollMe"></button>
                </fieldset>
            </form>

            <div class="section">
                <h2>Or select a tag</h2>
                <ul class="tag-list_1 clearfix">
                    <li class="tag"><a href="#">Action</a></li>
                    <li class="tag"><a href="#">Attention</a></li>
                    <li class="tag"><a href="#">Emotion</a></li>
                    <li class="tag"><a href="#">Executive/cognitive control</a></li>
                    <li class="tag"><a href="#">Language</a></li>
                    <li class="tag"><a href="#">Learning and memory</a></li>
                    <li class="tag"><a href="#">Perception</a></li>
                    <li class="tag"><a href="#">Reasoning and decision making</a></li>
                    <li class="tag"><a href="#">Social function</a></li>
                    <li class="tag"><a href="#">Motivation</a></li>
                </ul>
            </div>

        </div><!-- /content -->
        
    </div><!-- /core -->

</div><!-- /content-section -->

<?php include('inc/bottom-nav.logged.inc.php'); ?>

<?php include('inc/footer.inc.php'); ?>
    
    <!-- START : scripts -->
    <?php include('inc/scripts.inc.php'); ?>
    <!-- END : scripts -->
    
</body>
</html>