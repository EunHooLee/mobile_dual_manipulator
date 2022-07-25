; Auto-generated. Do not edit!


(cl:in-package mservo_msg-msg)


;//! \htmlinclude traj_2d.msg.html

(cl:defclass <traj_2d> (roslisp-msg-protocol:ros-message)
  ((traj_2d
    :reader traj_2d
    :initarg :traj_2d
    :type (cl:vector mservo_msg-msg:traj_1d)
   :initform (cl:make-array 50 :element-type 'mservo_msg-msg:traj_1d :initial-element (cl:make-instance 'mservo_msg-msg:traj_1d))))
)

(cl:defclass traj_2d (<traj_2d>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <traj_2d>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'traj_2d)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mservo_msg-msg:<traj_2d> is deprecated: use mservo_msg-msg:traj_2d instead.")))

(cl:ensure-generic-function 'traj_2d-val :lambda-list '(m))
(cl:defmethod traj_2d-val ((m <traj_2d>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mservo_msg-msg:traj_2d-val is deprecated.  Use mservo_msg-msg:traj_2d instead.")
  (traj_2d m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <traj_2d>) ostream)
  "Serializes a message object of type '<traj_2d>"
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'traj_2d))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <traj_2d>) istream)
  "Deserializes a message object of type '<traj_2d>"
  (cl:setf (cl:slot-value msg 'traj_2d) (cl:make-array 50))
  (cl:let ((vals (cl:slot-value msg 'traj_2d)))
    (cl:dotimes (i 50)
    (cl:setf (cl:aref vals i) (cl:make-instance 'mservo_msg-msg:traj_1d))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<traj_2d>)))
  "Returns string type for a message object of type '<traj_2d>"
  "mservo_msg/traj_2d")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'traj_2d)))
  "Returns string type for a message object of type 'traj_2d"
  "mservo_msg/traj_2d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<traj_2d>)))
  "Returns md5sum for a message object of type '<traj_2d>"
  "1e758c7f7f248e577c2b0cf954d10ea6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'traj_2d)))
  "Returns md5sum for a message object of type 'traj_2d"
  "1e758c7f7f248e577c2b0cf954d10ea6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<traj_2d>)))
  "Returns full string definition for message of type '<traj_2d>"
  (cl:format cl:nil "traj_1d[50] traj_2d~%~%================================================================================~%MSG: mservo_msg/traj_1d~%float64[7] traj~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'traj_2d)))
  "Returns full string definition for message of type 'traj_2d"
  (cl:format cl:nil "traj_1d[50] traj_2d~%~%================================================================================~%MSG: mservo_msg/traj_1d~%float64[7] traj~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <traj_2d>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'traj_2d) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <traj_2d>))
  "Converts a ROS message object to a list"
  (cl:list 'traj_2d
    (cl:cons ':traj_2d (traj_2d msg))
))
