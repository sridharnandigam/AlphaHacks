//
//  ContentView.swift
//  AlphaHacks
//
//  Created by Arpan Dhatt on 6/11/21.
//

import SwiftUI

struct ContentView: View {
    @EnvironmentObject var appState: AppState
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
        }.onChange(of: image, perform: { value in
            print("Image captured!")
            showSheet = true
            appState.POST_image(image: image!)
        }).sheet(isPresented: $showSheet, content: {
            if appState.companies.count > 1 && appState.companies[0] == "Test Company 1" {
                LoadingPage()
            } else {
                NavigationView {
                    MainResultsPage()
                }
            }
        })
    }
}
