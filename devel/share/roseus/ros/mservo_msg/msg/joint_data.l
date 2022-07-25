;; Auto-generated. Do not edit!


(when (boundp 'mservo_msg::joint_data)
  (if (not (find-package "MSERVO_MSG"))
    (make-package "MSERVO_MSG"))
  (shadow 'joint_data (find-package "MSERVO_MSG")))
(unless (find-package "MSERVO_MSG::JOINT_DATA")
  (make-package "MSERVO_MSG::JOINT_DATA"))

(in-package "ROS")
;;//! \htmlinclude joint_data.msg.html


(defclass mservo_msg::joint_data
  :super ros::object
  :slots (_pos ))

(defmethod mservo_msg::joint_data
  (:init
   (&key
    ((:pos __pos) (make-array 7 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _pos __pos)
   self)
  (:pos
   (&optional __pos)
   (if __pos (setq _pos __pos)) _pos)
  (:serialization-length
   ()
   (+
    ;; int32[7] _pos
    (* 4    7)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[7] _pos
     (dotimes (i 7)
       (write-long (elt _pos i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[7] _pos
   (dotimes (i (length _pos))
     (setf (elt _pos i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     )
   ;;
   self)
  )

(setf (get mservo_msg::joint_data :md5sum-) "84fce591d749df1cf35b0205dc6eac71")
(setf (get mservo_msg::joint_data :datatype-) "mservo_msg/joint_data")
(setf (get mservo_msg::joint_data :definition-)
      "int32[7] pos

")



(provide :mservo_msg/joint_data "84fce591d749df1cf35b0205dc6eac71")


