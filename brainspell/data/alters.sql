-- 06/05/2012

ALTER TABLE `papers_tag`
    CHANGE `created_by_id` `created_by_id` INT( 11 ) NULL ;

-- 08/05/2012

ALTER TABLE `papers_label`
    ADD `is_predefined` TINYINT( 1 ) DEFAULT 0 ;

-- 14/05/2012

ALTER TABLE `papers_label`
    ADD `cognitive_atlas_id` VARCHAR( 32 ) NULL ;

ALTER TABLE `papers_taginstance`
    CHANGE `user_id` `user_id` INT( 11 ) NULL ; 

-- 15/05/2012

ALTER TABLE `papers_tag`
    ADD `level` TINYINT( 1 ) NOT NULL DEFAULT '1' AFTER `created_by_id` ;

-- 28/05/2012

ALTER TABLE `papers_tag`
    ADD `parent_id` INT( 11 ) NULL AFTER `level` ;

ALTER TABLE `papers_paper`
    ADD `source` LONGTEXT NULL AFTER `abstract` ;
    