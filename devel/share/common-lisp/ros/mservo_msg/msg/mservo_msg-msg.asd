
(cl:in-package :asdf)

(defsystem "mservo_msg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "joint_data" :depends-on ("_package_joint_data"))
    (:file "_package_joint_data" :depends-on ("_package"))
    (:file "joint_queue" :depends-on ("_package_joint_queue"))
    (:file "_package_joint_queue" :depends-on ("_package"))
    (:file "traj_1d" :depends-on ("_package_traj_1d"))
    (:file "_package_traj_1d" :depends-on ("_package"))
    (:file "traj_2d" :depends-on ("_package_traj_2d"))
    (:file "_package_traj_2d" :depends-on ("_package"))
  ))