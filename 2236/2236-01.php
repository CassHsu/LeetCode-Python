<?php
class Solution {
    function checkTree($root) {
        return $root->val === $root->left->val + $root->right->val;
    }
}
