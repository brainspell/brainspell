<?php include('inc/head.inc.php'); ?>

<body>

<?php include('inc/top-nav.logged.inc.php'); ?>

<div class="content-section">

    <?php include('inc/header.inc.php'); ?>

    <div id="core">

        <div class="content">

            <div class="section">

                <h2>My profile</h2>

                <table class="table-profile">
                    <tr>
                        <th>Identifiant</th>
                        <td>
                            johndoe@domain.com
                            <form action="#" id="form-1">
                                <p>
                                    <label for="id">Your new identifiant</label>
                                    <input id="id" type="text">
                                    <button type="submit" class="button">OK</button>
                                </p>
                            </form>
                        </td>
                        <td class="txtR"><a href="#form-1" class="picto edit-link">Edit this</a></td>
                    </tr>
                    <tr>
                        <th>Password</th>
                        <td>
                            ●●●●●●●●●
                            <form action="#" id="form-2">
                                <p>
                                    <label for="pwd">Your new password</label>
                                    <input id="pwd" type="text">
                                    <button type="submit" class="button">OK</button>
                                </p>
                            </form>
                        </td>
                        <td class="txtR"><a href="#form-2" class="picto edit-link">Edit this</a></td>
                    </tr>
                    <tr>
                        <th>About me</th>
                        <td>
                            <p class="description">Etiam ac elit risus. Nam nulla arcu, placerat eget egestas ac, ornare in magna. Vestibulum cursus laoreet tortor, a mattis felis condimentum eu. Fusce nec rhoncus diam. Sed eu nisl et ligula placerat dapibus. Integer sed lacus sit amet nulla commodo adipiscing non sed lacus. Phasellus pharetra tincidunt magna nec mattis. Nullam semper imperdiet eros.</p>
                            <form action="#" id="form-3">
                                <p>
                                    <label for="description">Your new description</label>
                                    <textarea id="description" cols="30" rows="3"></textarea>
                                    <button type="submit" class="button">OK</button>
                                </p>
                            </form>
                        </td>
                        <td class="txtR"><a href="#form-3" class="picto edit-link">Edit this</a></td>
                    </tr>
                </table>

            </div><!-- /section -->

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