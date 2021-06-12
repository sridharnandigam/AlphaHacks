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
    @State private var showSheet = false
    
    var body: some View {
        ZStack {
            CustomCameraView(image: $image, didTapCapture: $didTapCapture).ignoresSafeArea(.all, edges: .top)
            VStack {
                Text("Take a Picture of Your Receipt or Product").font(.bold(.largeTitle)()).multilineTextAlignment(.center).shadow(color: Color.green, radius: 10, x: 0.0, y: 0.0).foregroundColor(.white)
                Spacer()
            }
        }.onChange(of: didTapCapture, perform: { value in
            if didTapCapture == true {
                print("Image captured!")
                showSheet = true
                didTapCapture = false
            }
        }).sheet(isPresented: $showSheet, content: {
            LoadingPage()
        })
    }
}
