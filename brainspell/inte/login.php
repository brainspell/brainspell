<?php include('inc/head.inc.php'); ?>

<body>

<?php include('inc/top-nav.not-logged.inc.php'); ?>

<div class="content-section">

    <?php include('inc/header.inc.php'); ?>

    <div id="core">

        <div class="content">

            <div class="section">

                <h2><strong>Log in</strong> or <strong>Create an account</strong></h2>

                <form action="#" id="log-in" class="form-generic">
                    <p class="clearfix">
                        <label for="id">Identifiant</label>
                        <input id="id" type="text" title="email@provider.ext">
                    </p>
                    <p class="clearfix">
                        <label for="pwd">Password</label>
                        <input id="pwd" type="password" title="your password">
                    </p>
                    <p class="submit">
                        <button type="submit" class="button">Log in</button>
                        <span class="or">or</span>
                        <button type="submit" class="button">Create a new account with this id/password</button>
                    </p>
                    <p class="forgot"><a href="#">Forgot your password?</a></p>
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