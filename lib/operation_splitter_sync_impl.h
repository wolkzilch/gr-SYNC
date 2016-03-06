/* -*- c++ -*- */
/* 
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_SYNC_OPERATION_SPLITTER_SYNC_IMPL_H
#define INCLUDED_SYNC_OPERATION_SPLITTER_SYNC_IMPL_H
#define AVG_SIZE 3

#include <SYNC/operation_splitter_sync.h>


namespace gr {
  namespace SYNC {

    class operation_splitter_sync_impl : public operation_splitter_sync
    {
     private:
      // Nothing to declare in this block.
      // std::array<float, 1024> real_vec;
      // std::array<float, 1024> imag_vec;
      float real_vec[AVG_SIZE];
      float imag_vec[AVG_SIZE];
      float real_avg;
      float imag_avg;
      size_t counter;

     public:
      operation_splitter_sync_impl();
      ~operation_splitter_sync_impl();

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace SYNC
} // namespace gr

#endif /* INCLUDED_SYNC_OPERATION_SPLITTER_SYNC_IMPL_H */

