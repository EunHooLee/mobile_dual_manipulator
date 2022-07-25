
(cl:in-package :asdf)

(defsystem "ethercat_test-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "pos" :depends-on ("_package_pos"))
    (:file "_package_pos" :depends-on ("_package"))
    (:file "trajectory" :depends-on ("_package_trajectory"))
    (:file "_package_trajectory" :depends-on ("_package"))
    (:file "vel" :depends-on ("_package_vel"))
    (:file "_package_vel" :depends-on ("_package"))
  ))