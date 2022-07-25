; Auto-generated. Do not edit!


(cl:in-package mservo_msg-msg)


;//! \htmlinclude joint_data.msg.html

(cl:defclass <joint_data> (roslisp-msg-protocol:ros-message)
  ((pos
    :reader pos
    :initarg :pos
    :type (cl:vector cl:integer)
   :initform (cl:make-array 7 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass joint_data (<joint_data>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <joint_data>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'joint_data)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mservo_msg-msg:<joint_data> is deprecated: use mservo_msg-msg:joint_data instead.")))

(cl:ensure-generic-function 'pos-val :lambda-list '(m))
(cl:defmethod pos-val ((m <joint_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mservo_msg-msg:pos-val is deprecated.  Use mservo_msg-msg:pos instead.")
  (pos m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <joint_data>) ostream)
  "Serializes a message object of type '<joint_data>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'pos))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <joint_data>) istream)
  "Deserializes a message object of type '<joint_data>"
  (cl:setf (cl:slot-value msg 'pos) (cl:make-array 7))
  (cl:let ((vals (cl:slot-value msg 'pos)))
    (cl:dotimes (i 7)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<joint_data>)))
  "Returns string type for a message object of type '<joint_data>"
  "mservo_msg/joint_data")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'joint_data)))
  "Returns string type for a message object of type 'joint_data"
  "mservo_msg/joint_data")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<joint_data>)))
  "Returns md5sum for a message object of type '<joint_data>"
  "84fce591d749df1cf35b0205dc6eac71")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'joint_data)))
  "Returns md5sum for a message object of type 'joint_data"
  "84fce591d749df1cf35b0205dc6eac71")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<joint_data>)))
  "Returns full string definition for message of type '<joint_data>"
  (cl:format cl:nil "int32[7] pos~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'joint_data)))
  "Returns full string definition for message of type 'joint_data"
  (cl:format cl:nil "int32[7] pos~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <joint_data>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'pos) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <joint_data>))
  "Converts a ROS message object to a list"
  (cl:list 'joint_data
    (cl:cons ':pos (pos msg))
))
