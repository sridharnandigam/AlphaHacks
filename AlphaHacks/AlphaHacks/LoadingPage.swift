//
//  LoadingPage.swift
//  AlphaHacks
//
//  Created by Arpan Dhatt on 6/12/21.
//

import SwiftUI

struct LoadingPage: View {
    private var loading_info = [
        ("doc.text.viewfinder","Scanning Image for Brands..."),
        ("text.magnifyingglass","Finding Competitors..."),
        ("gearshape","Reading Sustainability Index..."),
        ("newspaper","Fetching News Articles...")
    ]
    @State private var item = 0;
    let timer = Timer.publish(every: 1, on: .main, in: .common).autoconnect()
    var body: some View {
        VStack {
            ForEach(0..<loading_info.count) {info in
                VStack {
                    Image(systemName: loading_info[info].0).resizable().frame(width: 100, height: 100, alignment: .center).foregroundColor(.green).shadow(color: Color.green, radius: item == info ? 10 : 0)
                    if (item == info) {
                        Text(loading_info[info].1).foregroundColor(.green)
                    }
                }.scaleEffect(item == info ? 1.0 : 0.5).animation(.easeInOut)
            }
        }
        .onReceive(timer, perform: { input in
            item = (item + 1) % 4
        })
    }
}

struct LoadingPage_Previews: PreviewProvider {
    static var previews: some View {
        LoadingPage()
    }
}
