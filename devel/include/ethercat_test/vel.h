// Generated by gencpp from file ethercat_test/vel.msg
// DO NOT EDIT!


#ifndef ETHERCAT_TEST_MESSAGE_VEL_H
#define ETHERCAT_TEST_MESSAGE_VEL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ethercat_test
{
template <class ContainerAllocator>
struct vel_
{
  typedef vel_<ContainerAllocator> Type;

  vel_()
    : velocity()  {
      velocity.assign(0);
  }
  vel_(const ContainerAllocator& _alloc)
    : velocity()  {
  (void)_alloc;
      velocity.assign(0);
  }



   typedef boost::array<int32_t, 4>  _velocity_type;
  _velocity_type velocity;





  typedef boost::shared_ptr< ::ethercat_test::vel_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ethercat_test::vel_<ContainerAllocator> const> ConstPtr;

}; // struct vel_

typedef ::ethercat_test::vel_<std::allocator<void> > vel;

typedef boost::shared_ptr< ::ethercat_test::vel > velPtr;
typedef boost::shared_ptr< ::ethercat_test::vel const> velConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ethercat_test::vel_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ethercat_test::vel_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ethercat_test::vel_<ContainerAllocator1> & lhs, const ::ethercat_test::vel_<ContainerAllocator2> & rhs)
{
  return lhs.velocity == rhs.velocity;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ethercat_test::vel_<ContainerAllocator1> & lhs, const ::ethercat_test::vel_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ethercat_test

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ethercat_test::vel_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ethercat_test::vel_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ethercat_test::vel_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ethercat_test::vel_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ethercat_test::vel_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ethercat_test::vel_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ethercat_test::vel_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f8dbe9fe5f891a8fdba5d30d5afaa9f6";
  }

  static const char* value(const ::ethercat_test::vel_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf8dbe9fe5f891a8fULL;
  static const uint64_t static_value2 = 0xdba5d30d5afaa9f6ULL;
};

template<class ContainerAllocator>
struct DataType< ::ethercat_test::vel_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ethercat_test/vel";
  }

  static const char* value(const ::ethercat_test::vel_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ethercat_test::vel_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32[4] velocity\n"
;
  }

  static const char* value(const ::ethercat_test::vel_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ethercat_test::vel_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.velocity);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct vel_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ethercat_test::vel_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ethercat_test::vel_<ContainerAllocator>& v)
  {
    s << indent << "velocity[]" << std::endl;
    for (size_t i = 0; i < v.velocity.size(); ++i)
    {
      s << indent << "  velocity[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.velocity[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ETHERCAT_TEST_MESSAGE_VEL_H