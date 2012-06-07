<?php include('inc/head.inc.php'); ?>

<body>

<?php include('inc/top-nav.not-logged.inc.php'); ?>

<div class="content-section">

    <?php include('inc/header.inc.php'); ?>

    <div id="core">

        <div class="content">

            <div class="section">

                <h2>Forgot your password?</h2>

                <form action="#" id="forgot" class="form-generic">
                    <p class="clearfix">
                        <label for="id">Enter your email and we will send you another one</label>
                        <input id="id" type="text" title="email@provider.ext">
                        <button type="submit" class="button">Go!</button>
                    </p>
                </form>

            </div><!-- /section -->

        </div><!-- /content -->

    </div><!-- /core -->

</div><!-- /content-section -->

<?php include('inc/bottom-nav.not-logged.inc.php'); ?>

<?php include('inc/footer.inc.php'); ?>
    
    <!-- START : scripts -->
    <?php include('inc/scripts.inc.php'); ?>
    <!-- END : scripts -->
    
</body>
</html>