
(cl:in-package :asdf)

(defsystem "dxl_gripper-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "GripperDist" :depends-on ("_package_GripperDist"))
    (:file "_package_GripperDist" :depends-on ("_package"))
  ))