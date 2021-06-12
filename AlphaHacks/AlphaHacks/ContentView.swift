//
//  ContentView.swift
//  AlphaHacks
//
//  Created by Arpan Dhatt on 6/11/21.
//

import SwiftUI

struct ContentView: View {
    @State private var image = UIImage(systemName: "cake")
    @State private var didTapCapture = false
    @State private var color = Color.red
    
    var body: some View {
        ZStack {
            CustomCameraView(image: $image, didTapCapture: $didTapCapture)
            Circle().fill(color).frame(width: 100, height: 100)
        }.onChange(of: didTapCapture, perform: { value in
            if didTapCapture == true {
                print("Image captured!")
                
            }
        })
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
