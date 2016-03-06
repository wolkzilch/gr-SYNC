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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "operation_splitter_sync_impl.h"
#include <cstdlib>

namespace gr {
  namespace SYNC {

    operation_splitter_sync::sptr
    operation_splitter_sync::make()
    {
      return gnuradio::get_initial_sptr
        (new operation_splitter_sync_impl());
    }

    // PRIVATE CONSTRUCTOR
    operation_splitter_sync_impl::operation_splitter_sync_impl()
      : gr::sync_decimator("operation_splitter_sync",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),     // these might need to be 'char'
              gr::io_signature::make(2, 2, sizeof(gr_complex)), 2)
    {
      for(int i = 0; i<AVG_SIZE; i++){\
        real_vec[i] = 0;
        imag_vec[i] = 0;
      }
      real_avg = 0.0;
      imag_avg = 0.0;
      counter = 0;
    }

    // VIRTUAL DISTRUCTOR
    operation_splitter_sync_impl::~operation_splitter_sync_impl()
    {
    }

    int
    operation_splitter_sync_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      size_t item_size = output_signature()->sizeof_stream_item(0);

      const gr_complex *in = (const gr_complex *)input_items[0];
      gr_complex **outv = (gr_complex **)&output_items[0];
      int nstreams = output_items.size();

      // pointers need to move? Hmm.. maybe a circular buffer?
      for (int i = 0; i < noutput_items; i++) {
        for (int j = 0; j < nstreams; j++) {

          if(j == 0){
            // PASSTHROUGH CHANNEL
            outv[j][0] = in[0];   // push a single value
          }else{
            // OPERATION CHANNEL: N-point Average
            imag_vec[counter % AVG_SIZE] = in[0].imag();
            real_vec[counter % AVG_SIZE] = in[0].real();

            // perform average
            for(int k = 0; k < AVG_SIZE; k++){
              real_avg += in[0].real();
              imag_avg += in[0].imag();
            }
            real_avg = real_avg/AVG_SIZE;
            imag_avg = imag_avg/AVG_SIZE;

            gr_complex temp_val(real_avg,imag_avg);

            outv[j][0] = temp_val;  // push a single value
          }
          outv[j] += 1;             // eight bytes for gr_complex type
          in += 1;                  // eight bytes for gr_complex type

          // THE ORIGINAL CODE
          // memcpy(outv[j], in, item_size);
          // outv[j] += item_size;
          // in += item_size;
        }
        counter += 1;
      }

      return noutput_items;
    }

  } /* namespace SYNC */
} /* namespace gr */

