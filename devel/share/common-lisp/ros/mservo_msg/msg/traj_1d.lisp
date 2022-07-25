; Auto-generated. Do not edit!


(cl:in-package mservo_msg-msg)


;//! \htmlinclude traj_1d.msg.html

(cl:defclass <traj_1d> (roslisp-msg-protocol:ros-message)
  ((traj
    :reader traj
    :initarg :traj
    :type (cl:vector cl:float)
   :initform (cl:make-array 7 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass traj_1d (<traj_1d>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <traj_1d>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'traj_1d)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mservo_msg-msg:<traj_1d> is deprecated: use mservo_msg-msg:traj_1d instead.")))

(cl:ensure-generic-function 'traj-val :lambda-list '(m))
(cl:defmethod traj-val ((m <traj_1d>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mservo_msg-msg:traj-val is deprecated.  Use mservo_msg-msg:traj instead.")
  (traj m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <traj_1d>) ostream)
  "Serializes a message object of type '<traj_1d>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'traj))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <traj_1d>) istream)
  "Deserializes a message object of type '<traj_1d>"
  (cl:setf (cl:slot-value msg 'traj) (cl:make-array 7))
  (cl:let ((vals (cl:slot-value msg 'traj)))
    (cl:dotimes (i 7)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<traj_1d>)))
  "Returns string type for a message object of type '<traj_1d>"
  "mservo_msg/traj_1d")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'traj_1d)))
  "Returns string type for a message object of type 'traj_1d"
  "mservo_msg/traj_1d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<traj_1d>)))
  "Returns md5sum for a message object of type '<traj_1d>"
  "58e9b5284e3c4cd3c99f99337b97f52c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'traj_1d)))
  "Returns md5sum for a message object of type 'traj_1d"
  "58e9b5284e3c4cd3c99f99337b97f52c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<traj_1d>)))
  "Returns full string definition for message of type '<traj_1d>"
  (cl:format cl:nil "float64[7] traj~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'traj_1d)))
  "Returns full string definition for message of type 'traj_1d"
  (cl:format cl:nil "float64[7] traj~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <traj_1d>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'traj) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <traj_1d>))
  "Converts a ROS message object to a list"
  (cl:list 'traj_1d
    (cl:cons ':traj (traj msg))
))
